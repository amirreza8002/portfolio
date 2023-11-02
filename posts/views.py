from django.shortcuts import render, Http404

from .models import Post


def post_list_view(request):
    posts = Post.published.all()
    return render(request, "posts/post_list.html", {"posts": posts})


def post_detail_view(request, slug):
    post = Post.published.filter(slug=slug)
    if post:
        return render(request, "posts/post_detail.html", {"post": post})
    else:
        raise Http404
