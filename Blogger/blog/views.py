from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from blog import models
from .models import Post
from django.contrib.auth import authenticate, login, logout




def signup(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        password = request.POST.get('upassword')
        confirm_password = request.POST.get('confirm_password')
        if User.objects.filter(username=name).exists():
            return render(request, 'blog/signup.html', {'error': 'Username already exists'})
        if password != confirm_password:
            return render(request, 'blog/signup.html', {'error': 'Passwords do not match'})
        newUser = User.objects.create_user(username=name, password=password)
        newUser.save()
        return redirect('/login/')
    return render(request, 'blog/signup.html')




def loginn(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        password = request.POST.get('upassword')
        userr = authenticate(request, username=name, password=password)
        if userr is not None:
            login(request, userr)
            return redirect('/home/')
        else:
            return redirect('/login')

    return render(request, 'blog/login.html')




def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)



def newPost(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        npost = models.Post(title=title, content=content, author=request.user)
        npost.save()
        return redirect('/home')
    
    return render(request, 'blog/newpost.html')




def myPost(request):
    context = {
        'posts': Post.objects.filter(author= request.user)
    }
    return render(request, 'blog/mypost.html', context)



def signout(request):
    logout(request)
    return redirect('/login/')


def updatePost(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.author != request.user:
        return redirect('/home/')
    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('/home/')
    return render(request, 'blog/updatepost.html', {'post': post})

def deletePost(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.author != request.user and not request.user.is_staff:
        return redirect('/home/')
    post.delete()
    return redirect('/home/')

