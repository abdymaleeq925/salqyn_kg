from django.shortcuts import render
from .models import Post, Category


def index(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    context = {
        "posts": posts,
        "categories": categories,
    }
    return render(request, "index.html", context=context)


def get_post_list(request):
    posts = Post.objects.filter(is_active=True)
    context = {
        "posts": posts,
    }
    return render(request, "post_list.html", context=context)
