from django.shortcuts import render, get_object_or_404

from .models import Post, Group
from .constants import POSTS_ON_PAGE


def index(request):
    """View функция для index."""
    posts = Post.objects.order_by('-pub_date')[:POSTS_ON_PAGE]
    context = {
        'posts': posts,
    }

    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    """View функция для group_posts."""
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:POSTS_ON_PAGE]
    context = {
        'group': group,
        'posts': posts,
    }

    return render(request, 'posts/group_list.html', context)
