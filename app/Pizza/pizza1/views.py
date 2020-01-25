from django.shortcuts import render

# Create your views here.
from .models import Post, Tag



def Project_Function(request):
    pizza = Post.objects.all()
    return render(request, 'Pizza/index.html', context={'pizza':pizza})

def pizza_detail(request, slug):
    pizza = Post.objects.get(slug__iexact= slug)
    return render(request, 'Pizza/pizza_detail.html', context={'pizza':pizza})

def pizza_detail(request, slug):
    pizza = Post.objects.get(slug__iexact= slug)
    return render(request, 'Pizza/pizza_detail.html', context={'pizza':pizza})

def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'Pizza/tags_list.html', context = {'tags': tags})

def tag_detail(request, slug):
    tag = Tag.objects.get(slug__iexact=slug)

    # tags = Tag.objects.all()
    return render(request, 'Pizza/tag_detail.html', context={'tag':tag})