from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def home(request):
    posts1 = Post.objects
    return render(request, 'log/home.html', {'posts2':posts1})