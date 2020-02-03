from django.shortcuts import render
from django.views.generic import View
# Create your views here.
from .models import *
from django.shortcuts import get_object_or_404
from .utils import ObjectDetailMixin
from .forms import TagForm, PostForm

from django.shortcuts import redirect

from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse


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
        return render(request, self.template, context={'form': bound_form, self.model.__name__.lower(): obj})

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.model_form(request.POST, instance=obj)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request, self.template, context={'form': bound_form, self.model.__name__.lower(): obj})


class ObjectDeleteMixin:
    model = None
    template = None
    redirect_url = None

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__: obj})

    def post(self, request, slug):
        odj = self.model.objects.get(slug__iexact=slug)
        odj.delete()
        return render(reverse(self.redirect_url))


def pizza_count(request):
    pizza = Post.objects.all()
    search_query = request.GET.get('search1', '')
    return render(request, 'Pizza/Count.html', context={'posts': pizza, 'search1': search_query})


# def basket_adding1(request):
#     tags = ProductInBasket.objects.all()
#     return render(request, 'Pizza/Count.html', context = {'tags': tags})


def pizza_list(request):
    search_query = request.GET.get('search', '')
    # search_count = request.POST.post('search1', '')
    #
    # if search_count.is_valid():
    #     pass
    #

    if search_query:
        pizza = Post.objects.filter(Q(title__icontains=search_query) | Q(body__icontains=search_query))
    else:
        pizza = Post.objects.all()

    pizza = Post.objects.all()
    paginator = Paginator(pizza, 2)

    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()

    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {
        'page_object': page,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url
    }

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    print(request.session.session_key)

    return render(request, 'Pizza/index.html', context=context)


# def pizza_detail(request, slug):
#     pizza = Post.objects.get(slug__iexact= slug)
#     return render(request, 'Pizza/pizza_detail.html', context={'pizza':pizza})


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'Pizza/pizza_detail.html'

    # def get(self,request,slug):
    #     pizza = get_object_or_404(Post,slug__iexact=slug)
    #     # pizza = Post.objects.get(slug__iexact=slug)
    #     return render(request, 'Pizza/pizza_detail.html', context={'post': pizza})


# def pizza_detail(request, slug):
#     pizza = Post.objects.get(slug__iexact= slug)
#     return render(request, 'Pizza/pizza_detail.html', context={'pizza':pizza})


class PostCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    model_form = PostForm
    template = 'Pizza/pizza_create_form.html'
    raise_exception = True

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


class PostUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Post
    model_form = PostForm
    template = 'Pizza/pizza_update_form.html'
    raise_exception = True


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'Pizza/tags_list.html', context={'tags': tags})


class TagDetail(ObjectDetailMixin, View):
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

class TagCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    model_form = TagForm
    template = 'Pizza/tag_create.html'
    raise_exception = True

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


class TagUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Tag
    model_form = TagForm
    template = 'Pizza/tag_update_form.html'
    raise_exception = True

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


class TagDelete(LoginRequiredMixin, View):
    raise_exception = True

    # model = Tag
    # template = 'Pizza/tag_delete_form.html'
    # redirect_url = 'tags_list_url'

    def get(self, request, slug):
        tag = Tag.objects.get(slug__iexact=slug)
        return render(request, 'Pizza/tag_delete_form.html', context={'tag': tag})

    def post(self, request, slug):
        tag = Tag.objects.get(slug__iexact=slug)
        tag.delete()
        return render(reverse('tags_list_url'))


class PostDelete(LoginRequiredMixin, View):
    raise_exception = 'true'

    # model = Tag
    # template = 'Pizza/tag_delete_form.html'
    # redirect_url = 'tags_list_url'

    def get(self, request, slug):
        post = Post.objects.get(slug__iexact=slug)
        return render(request, 'Pizza/pizza_delete_form.html', context={'post': post})

    def post(self, request, slug):
        pizz = Post.objects.get(slug__iexact=slug)
        pizz.delete()
        return render(reverse('pizza_list_url'))


def basket_adding(request):
    return_dict = dict()
    session_key = request.session.session_key
    print(request.POST)
    data = request.POST
    products_name = data.get('products_name')
    print(products_name)
    nmb = data.get('nmb')
    is_delete = data.get("is_delete")
    if is_delete == 'true':

        product = ProductInBasket.objects.filter(products_name=products_name).update(is_active=False)
        # product.is_active = False
        # product.save(force_update=True)
    else:



        new_product, created = ProductInBasket.objects.get_or_create(session_key=session_key, products_name=products_name, is_active=True,
                                                                     defaults={'nmb': nmb})

        if not created:

            new_product.nmb += int(nmb)
            new_product.save(force_update=True)


    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True)
    products_total_nmb = products_in_basket.count()

    return_dict["products_total_nmb"] = products_total_nmb

    return_dict["products"] = list()

    for item in products_in_basket:
            product_dict = dict()

            product_dict["products_name"] = item.products_name
            product_dict["nmb"] = item.nmb
            return_dict["products"].append(product_dict)

    return JsonResponse(return_dict)
    # return render(request, 'Pizza/Count.html', context={'nmb': new_product})


def checkout(request):
    session_key = request.session.session_key
    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True)
    return render(request, 'Pizza/checkout.html', context={'products_in_basket':products_in_basket})
