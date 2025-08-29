from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
from .models import Post

# Create your views here.
all_posts = [
]

def get_date(post):
    return post.get('date')

def starting_page(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request, 'blog/index.html', {'posts': latest_posts})


def posts(request):
    return render(request, 'blog/all-post.html', {'all_posts': all_posts})

def post_detail(request, slug):
    post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, 'blog/post-detail.html', {'post': post})