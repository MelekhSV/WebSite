from django.shortcuts import render
from django.views.generic import View
# Create your views here.
from .models import Post, Tag
from django.shortcuts import get_object_or_404
from .utils import ObjectDetailMixin


def pizza_list(request):
    pizza = Post.objects.all()
    return render(request, 'Pizza/index.html', context={'posts':pizza})

# def pizza_detail(request, slug):
#     pizza = Post.objects.get(slug__iexact= slug)
#     return render(request, 'Pizza/pizza_detail.html', context={'pizza':pizza})




class PostDetail(ObjectDetailMixin,View):
  model = Post
  template = 'Pizza/pizza_detail.html'

    # def get(self,request,slug):
    #     pizza = get_object_or_404(Post,slug__iexact=slug)
    #     # pizza = Post.objects.get(slug__iexact=slug)
    #     return render(request, 'Pizza/pizza_detail.html', context={'post': pizza})


# def pizza_detail(request, slug):
#     pizza = Post.objects.get(slug__iexact= slug)
#     return render(request, 'Pizza/pizza_detail.html', context={'pizza':pizza})

def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'Pizza/tags_list.html', context = {'tags': tags})



class TagDetail(ObjectDetailMixin,View):
    model = Tag
    template = 'Pizza/tag_detail.html'



    # def get(self,request,slug):
    #     def tag_detail(request, slug):
    #         tag = get_object_or_404(Tag, slug__iexact=slug)
    #         # tag = Tag.objects.get(slug__iexact=slug)
    #
    #         # tags = Tag.objects.all()
    #         return render(request, 'Pizza/tag_detail.html', context={'tag': tag})


# def tag_detail(request, slug):
#     tag = Tag.objects.get(slug__iexact=slug)
#
#     # tags = Tag.objects.all()
#     return render(request, 'Pizza/tag_detail.html', context={'tag':tag})
