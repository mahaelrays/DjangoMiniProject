from email import message
from django.shortcuts import render, redirect
from django.http.response import HttpResponseRedirect
from .forms import LoginForm,NewUserForm
from django.urls import reverse
from django.contrib.auth import login, logout,authenticate 
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib import messages
from appOne.forms import BlogPostForm,BlogPost,LoginForm,UpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from appOne.models import *

# Create your views here.
def home(request):    
    user = request.user
    if not user.is_authenticated:
            return render(request, "welcome.html")
    posts = BlogPost.objects.all()
    posts = BlogPost.objects.filter().order_by('-dateTime')
    return render(request, "home.html",{'posts':posts , 'user':user})
def welcome(request):
    return render(request, "welcome.html")

    
def blog(request):
    if request.method=="POST":
        user = request.user
        if not user.is_authenticated:
            return redirect("login")
        form = BlogPostForm(data=request.POST  , files=request.FILES )
        if form.is_valid():
            blogpost = form.save(commit=False)
            blogpost.author = request.user
            blogpost.save()
            return redirect("home")
    else:
        form=BlogPostForm()
    return render(request, "blog.html", {'form':form})
    

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            print('hhhhhhh')
            form.save()
            return redirect("login")
    form = NewUserForm()
    return render (request=request, template_name="register.html", context={"register_form":form})
    
def user_login(request):
        
    if request.method == 'POST':
        form = LoginForm(data = request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username,password=password)
        if user is not None :
            auth.login(request,user)
            posts = BlogPost.objects.all()
            return render(request, "home.html",{'posts':posts})
        
    form = LoginForm()
    return render(request, 'login.html', {'form':form})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
    
def delete_view(request,post_id):
    posts = BlogPost.objects.get(id=post_id)
    if request.method == "GET":
        posts.delete()
    posts = BlogPost.objects.all()
    return render(request,"home.html",{'posts':posts})
    

def about(request):  
    return render(request, "about.html")

def readmore(request,id):
    post = BlogPost.objects.get(id=id) 
    if request.method == 'GET':
        title = post.title 
        image = post.image
        author = post.author
        content = post.content
    return render(request,'readmore.html',{'image':image,'title':title,'author':author,'content':content})


def comment(request, post_id):
    print("commety")
    post = BlogPost.objects.filter(id=post_id).first()
    comments = None
    comments = post.comments.filter()
    if request.method=="POST":
        comments = comments.filter(blog=post)
        user = request.user
        content = request.POST.get('content','')
        blog_id =request.POST.get('blog_id','')
        comment = Comment( user=user,content = content,blog=post)
        comment.save()
    return render(request, "comment.html", {'post':post, 'comments':comments}) 

def update(request,id):
    post = BlogPost.objects.get(id = id)
    form = UpdateForm(instance=post)
    if request.method == 'POST':
        form = UpdateForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form = UpdateForm(instance=post)
    return render(request,'update.html',{'form':form}) 

def search(request):
    if request.method=="GET": 
        searched = request.GET.get('searched',default=" ")
        if searched:
            blogs = BlogPost.objects.filter(title__icontains=searched)
            return render(request, "search.html", {'searched':searched, 'blogs':blogs})