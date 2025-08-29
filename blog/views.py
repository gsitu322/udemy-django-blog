from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import ListView
from django.views import View
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse

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

class PostDetail(View):

    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        return render(request, "blog/post-detail.html", {
            "post": post,
            "post_tags": post.tags.all(),
            "comments": post.comments.all().order_by("-id"),
            "comment_form": CommentForm(),
        })

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = get_object_or_404(Post, slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()

            return HttpResponseRedirect(reverse("post_detail", args=[slug]))

        return render(request, "blog/post-detail.html", {
            "post": post,
            "post_tags": post.tags.all(),
            "comments": post.comments.all().order_by("-id"),
            "comment_form": comment_form,
        })