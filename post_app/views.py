from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import logout 
from django.contrib import auth
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def index(request):
    return render(request,'index.html')

def register(request):
    
    if request.method == 'POST':
        user_name=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        User.objects.create_user(username=user_name,first_name=first_name,last_name=last_name,email=email,password=password)
        return redirect('index')
    else:
        return render(request,'register.html')


def posts(request):
    post = Post.objects.values("id","user__username","post_message","created").order_by('-created')
    comments = Comment.objects.values("comment","post_id","user__username","created",'id').order_by('-created')
   
    #like_count = (Like.objects.values("post_id").annotate(like_count=Count('like')))
    #dislike_count = (Dislike.objects.values('post_id').annotate(dislike_count=Count('dislike')))
    
    comment_count = (Comment.objects.values('post_id').annotate(comment_count=Count('comment')))
    likes_count = (Post.objects.values('id').annotate(likes_count=Count('likes')))
    
    
    return render(request,'posts.html',{'post':post,'comments':comments,'comment_count':comment_count,'likes_count':likes_count})

def login(request):
    if request.method == 'POST':
            user_name = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(request, username=user_name, password=password)
            if user is not None:
                print(3)
                auth.login(request,user)
                print(5)
                return redirect('posts')
            else:
                msg = 'please enter a correct username and password'
                return render(request,'index.html',{'msg':msg})
    else:
        return redirect('index')
        
   
def compose_post(request):
    if request.method == 'POST':
        current_user = request.user
        post_message = Post.objects.create(
            user=current_user,
            post_message = request.POST['message']
        )
        print(3)
        return redirect('posts')
    
    

def comments(request,id):
    if request.method == 'POST':
        current_user = request.user
        print(current_user.id)
        post = Post.objects.get(id=id)
        print(post.id)
        comment=Comment.objects.create(
            user=current_user,
            post=post,
            comment=request.POST['comment']
        )    
    return redirect('posts')

def post_delete(request,id):
    user = request.user 
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('posts')
   
def like(request,id):
    if request.method == 'POST':
        user = request.user
        post = Post.objects.get(id=id)
        if Like.objects.filter(user=user, post=post).exists():
            return redirect('posts')
        else:
            newlike=Like(user=user,post=post)
            newlike.like += 1
            newlike.save()
            return redirect('posts')

def dislike(request,id):
    if request.method == 'POST':
        user = request.user
        post = Post.objects.get(id=id)
        print(1)
        if Dislike.objects.filter(user=user, post=post).exists():
           
            return redirect('posts')
        else:
            print(2)
            
            dislike = Dislike(user=user,post=post)
            dislike.dislike += 1
            dislike.save()
            return redirect('posts')

def delete_comment(request,id):
    user=request.user    
    comment= Comment.objects.get(id=id)    
    comment.delete()    
    return redirect('posts')
    
def logout(request):
    return redirect('index')

def like_post(request,id):
    post = get_object_or_404(Post,id=request.POST['post_id'])
    
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        
    else:
        post.likes.add(request.user)
        
        
    return redirect('posts')

