from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Profile, Post
from .forms import UserRegisterForm

def home(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, 'twitter/newsfeed.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserRegisterForm()

    context = {'form' : form}
    return render(request, 'twitter/register.html', context)
