from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import logout 
from django.contrib import auth
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
        return render(request,'index.html')
    else:
        return render(request,'register.html')


def post_listing(request):
    post = Post.objects.values("id","user__username","post_message","created").order_by('-created')
    
    comments = Comment.objects.values("comment","post_id","user__username","created",'id').order_by('-created')
    #like=Like.objects.values('like','post_id','user__username','id')
    comment= []
    for i in post :
        comment_count=Comment.objects.filter(post__id=i['id']).count()
        data={
            'post':i['id'],
            'comment_count':comment_count
            }
        comment.append(data)
    like= []
    for i in post :
        like_count=Like.objects.filter(post__id=i['id']).count()
        data={
            'post':i['id'],
            'like_count':like_count
            }
        like.append(data)

    dislike = []
    for i in post :
        dislike_count=Dislike.objects.filter(post__id=i['id']).count()
        data={
            'post':i['id'],
            'dislike_count':dislike_count
        }
        dislike.append(data)
    
    
    return render(request,'post_listing.html',{'post':post,'comment':comment,'like':like,'dislike':dislike,'comments':comments})

def login(request):
    if request.method == 'POST':
            user_name = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(request, username=user_name, password=password)
            if user is not None:
                print(3)
                auth.login(request,user)
                print(5)
                return redirect('post_listing')
            else:
                msg = 'please enter a correct username and password'
                return render(request,'index.html',{'msg':msg})
    else:
        return render(request,'index.html')
        
   
def compose_post(request):
    try:
        if request.method == 'POST':
            current_user = request.user
            post_message = Post.objects.create(
                user=current_user,
                post_message = request.POST['message']
            )
            print(3)
            return redirect('post_listing')
            print(4)
    except:
        print(5)
        return HttpResponse('<h2>404 page not found</h2>')

def comment_on_post(request,id):
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
    return redirect('post_listing')

def post_delete(request,id):
    try:
        user = request.user
        post = Post.objects.get(id=id,user=user)
        post.delete()
        return redirect('post_listing')

    except:
        return redirect('post_listing')

def like(request,id):
    if request.method == 'POST':
        user = request.user
        post = Post.objects.get(id=id)
        if Like.objects.filter(user=user, post=post).exists():
    
            return redirect('post_listing')
        else:
            newlike=Like(user=user,post=post)
            newlike.like += 1
            newlike.save()
            
            return redirect('post_listing')

def dislike(request,id):
    if request.method == 'POST':
        user = request.user
        post = Post.objects.get(id=id)
        print(1)
        if Dislike.objects.filter(user=user, post=post).exists():
           
            #decrease_like=Like(user=user,post=post)
            #print(3)
            #decrease_like.like -= 1
            #print(4)
            #decrease_like.save()
            #dislike = Dislike(user=user,post=post)
            #print(5)
            #dislike.dislike += 1
            #dislike.save()
            return redirect('post_listing')
        else:
            print(2)
            dislike = Dislike(user=user,post=post)
            dislike.dislike += 1
            dislike.save()
            like = Like(user=user,post=post,id=id)
            like.delete()
            print(3)
            

            
            print(4)
            return redirect('post_listing')


def logout(request):
    return redirect('index')

def delete_comment(request,id):
    try:
        user=request.user
        comment= Comment.objects.get(id=id,user=user)
        comment.delete()
        return redirect('post_listing')
    except:
        return redirect('post_listing')


