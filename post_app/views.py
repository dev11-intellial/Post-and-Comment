from django.shortcuts import render,HttpResponse,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import logout 
from django.contrib import auth
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
    post = Post.objects.all()
    like = Like.objects.all()
    return render(request,'post_listing.html',{'post':post,'like':like})

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

def logout(request):
    return redirect('index')


def post_with_comment(request,id):
    post = Post.objects.get(id=id) 
    comment = Comment.objects.filter(post=post)
    number_of_comment = comment.count()
    like = Like.objects.filter(post=post)
    number_of_like =like.count()
    return render(request,'comment_page.html',{'comment':comment,'post':post,'number_of_comment':number_of_comment,'number_of_like':number_of_like})




def delete_comment(request,id):
    try:
        user=request.user
        comment= Comment.objects.get(id=id,user=user)
        comment.delete()
        return redirect('post_listing')
    except:
        return redirect('post_listing')