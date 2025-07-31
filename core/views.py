from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post

@login_required(login_url='accounts:login')
def homeview(request):
    posts = Post.objects.filter(visibility="PUBLIC").order_by('-date_published')
    return render(request, 'core/core.html', {
        'posts': posts,
        })

@login_required(login_url='accounts:login')
def postcreationview(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post: Post = form.save(commit=False)
            post.publisher = request.user
            post.save()
            return redirect('core:home')
    
    form = PostForm()
    posts = Post.objects.filter(visibility="PUBLIC")
    return render(request, 'core/postcreation.html', {
        'form': form,
        'posts': posts,
        })
