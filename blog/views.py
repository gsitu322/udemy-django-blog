from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import ListView, DetailView

class StartingPageList(ListView):
    template_name = "blog/index.html"
    model = Post
    context_object_name = "posts"
    ordering = ["-date"]

    def get_queryset(self):
        query_set = super().get_queryset()
        query_set = query_set[:3]
        return query_set

class AllPosts(ListView):
    template_name = "blog/all-post.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "all_posts"

class PostDetail(DetailView):
    template_name = "blog/post-detail.html"
    model = Post
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_tags"] = self.object.tags.all()
        return context