from django.shortcuts import render,HttpResponse,redirect
from .models import *
from django.contrib.auth.models import User

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
    return render(request,'post_listing.html',{'post':post})

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
        #else:
            #msg = 'please enter a correct username and password'
            #return render(request,'index.html')
   
def compose_post(request):
    try:
        if request.method == 'POST':
            current_user = request.user
            #print( current_user.id)
            
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
    


def user_post(request):
    post = Post.objects.all()
    user = User.objects.filter(name=post)
    return render(request,'user_post.html',{'post':user})

def post_delete(request,id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('post_listing')

def sucess(request):
    return render(request,'sucess.html')

