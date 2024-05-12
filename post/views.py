from django.shortcuts import render
from .models import Category, Post, Like, Region, Agenda


def index(request):
    categories = Category.objects.all()
    agendas = Agenda.objects.all().order_by('created_at')
    regions = Region.objects.all()
    posts = Post.objects.all()
    latest_posts = Post.objects.all().order_by('created_at')[:8]
    context = {
        'categories': categories,
        'regions': regions,
        'posts': posts,
        'latest_posts': latest_posts,
        'agendas': agendas
    }
    return render(request, 'index.html', context)


def post_detail_view(request, slug):
    post = Post.objects.get(slug=slug)
    post.views += 1
    post.save()
    categories = Category.objects.all()
    agendas = Agenda.objects.all().order_by('created_at')
    regions = Region.objects.all()
    latest_posts = Post.objects.all().order_by('created_at')[:8]
    context = {
        'categories': categories,
        'regions': regions,
        'post': post,
        'latest_posts': latest_posts,
        'agendas': agendas
    }
    return render(request, 'post_detail.html', context)


def category_view(request, slug):
    categories = Category.objects.all()
    regions = Region.objects.all()
    category = Category.objects.get(slug=slug)
    posts = Post.objects.filter(category=category)
    latest_posts = Post.objects.all().order_by('created_at')[:8]
    context = {
        'categories': categories,
        'regions': regions,
        'posts': posts,
        'latest_posts': latest_posts,
    }
    return render(request, 'index.html', context)


def region_view(request, slug):
    region = Region.objects.get(slug=slug)
    categories = Category.objects.all()
    regions = Region.objects.all()
    posts = Post.objects.filter(region=region)
    latest_posts = Post.objects.all().order_by('created_at')[:8]
    context = {
        'categories': categories,
        'regions': regions,
        'posts': posts,
        'latest_posts': latest_posts,
    }
    return render(request, 'index.html', context)


