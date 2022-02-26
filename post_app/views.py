from django.shortcuts import render,HttpResponse
from .models import *
# Create your views here.
def index(request):
    return render(request,'index.html')

def post_listing(request):
    post = Post.objects.all()
    return render(request,'post_listing.html',{'post':post})

def login(request):
    
    try:
        if request.method == 'POST':
            print(1)
            user = User.objects.get(name=request.POST['name'])
            print(2)
            if user.name == request.POST['name'] and user.pin == request.POST['pin']:
                print(3)
                post = Post.objects.filter(user=user)
                return render(request,'new.html',{'post':post})
                print(4)

            else:
                
                return render(request,'index.html')
    except:
        print(5)
        msg = 'wgfuisg'
        return render(request,'index.html',{'msg':msg})

def new(request):
    post =Post.objects.all()
    user = User.objects.filter(name=post)
    
    return render(request,'new.html',{'post':user})


