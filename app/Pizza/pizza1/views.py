from django.shortcuts import render
from django.views.generic import View
# Create your views here.
from .models import Post, Tag
from django.shortcuts import get_object_or_404
from .utils import ObjectDetailMixin
from .forms import TagForm, PostForm

from django.shortcuts import redirect

from django.urls import reverse

class ObjectCreateMixin:
    model_form = None
    template = None


    def get(self, request):
        form = self.model_form()
        return render(request, self.template, context={'form': form})

    def post(self, request):
        bound_form = self.model_form(request.POST)
        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request, self.template, context={'form': bound_form})












class ObjectUpdateMixin:
    model = None
    model_form = None
    template = None

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.model_form(instance=obj)
        return render(request, self.template, context={'form':bound_form, self.model.__name__.lower():obj})


    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.model_form(request.POST, instance=obj)

        if bound_form.is_valid():
             new_obj = bound_form.save()
             return redirect(new_obj)
        return render(request, self.template, context={'form':bound_form, self.model.__name__.lower():obj})





class ObjectDeleteMixin:
    model = None
    template = None
    redirect_url = None
    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact = slug)
        return render(request, self.template, context={self.model.__name__:obj})

    def post(self, request, slug):
        odj = self.model.objects.get(slug__iexact=slug)
        odj.delete()
        return render(reverse(self.redirect_url))












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



class PostCreate(ObjectCreateMixin, View):
    model_form = PostForm
    template = 'Pizza/pizza_create_form.html'

    # def get(self,request):
    #     form = PostForm()
    #     return render(request, 'Pizza/pizza_create_form.html', context={'form':form})
    #
    # def post (self,request):
    #     bound_from = PostForm(request.POST)
    #     if bound_from.is_valid():
    #         new_post = bound_from.save()
    #         return redirect(new_post)
    #     return render(request, 'Pizza/pizza_create_form.html', context={'form': bound_from})


class PostUpdate(ObjectUpdateMixin, View):
    model = Post
    model_form = PostForm
    template = 'Pizza/pizza_update_form.html'






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

class TagCreate(ObjectCreateMixin,View):
    model_form = TagForm
    template = 'Pizza/tag_create.html'



     # def get(self,request):
     #     form = TagForm()
     #     return render(request, 'Pizza/tag_create.html', context={'form':form})
     #
     # def post(self,request):
     #
     #     bound_form = TagForm(request.POST)
     #     if bound_form.is_valid():
     #         new_tag = bound_form.save()
     #         return redirect(new_tag)
     #     return render(request, 'Pizza/tags_list.html', context={'form':bound_form} )

class TagUpdate(ObjectUpdateMixin, View):
    model = Tag
    model_form = TagForm
    template = 'Pizza/tag_update_form.html'

    # def get(self, request, slug):
    #     tag = Tag.objects.get(slug__iexact=slug)
    #     bound_form = TagForm(instance=tag)
    #     return render(request, 'Pizza/tag_update_form.html', context={'form':bound_form, 'tag':tag})
    #
    #
    # def post(self, request, slug):
    #     tag = Tag.objects.get(slug__iexact=slug)
    #     bound_form = TagForm(request.POST, instance=tag)
    #
    #     if bound_form.is_valid():
    #          new_tag = bound_form.save()
    #          return redirect(new_tag)

    #     return render(request, 'Pizza/tag_update_form', context={'form':bound_form, 'tag':tag})


class TagDelete(View):

    # model = Tag
    # template = 'Pizza/tag_delete_form.html'
    # redirect_url = 'tags_list_url'

    def get(self, request, slug):
        tag = Tag.objects.get(slug__iexact = slug)
        return render(request, 'Pizza/tag_delete_form.html', context={'tag':tag})

    def post(self, request, slug):
        tag = Tag.objects.get(slug__iexact=slug)
        tag.delete()
        return render(reverse('tags_list_url'))


class PostDelete(View):

    # model = Tag
    # template = 'Pizza/tag_delete_form.html'
    # redirect_url = 'tags_list_url'

    def get(self, request, slug):
        post = Post.objects.get(slug__iexact = slug)
        return render(request, 'Pizza/pizza_delete_form.html', context={'post':post})

    def post(self, request, slug):
        pizz = Post.objects.get(slug__iexact=slug)
        pizz.delete()
        return render(reverse('pizza_list_url'))
