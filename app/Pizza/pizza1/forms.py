from django import forms
from .models import *
from django.core.exceptions import ValidationError




class TagForm(forms.ModelForm):

    # title = forms.CharField(max_length=50)
    # slug = forms.CharField(max_length=50)
    #
    # title.widget.attrs.update({'class': 'form-control'})
    # slug.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Tag
        fields = ['title','slug']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'})
        }




    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug  == 'create':
            raise ValidationError('Slug may not be "Create"')
        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('Slug must be unique. We have "{}" slug alreade'.format(new_slug))

        return new_slug

    # def save(self): не используем т.к. MOdelForm сам сохраняет
    #     new_tag = Tag.objects.create(title=self.cleaned_data['title'], slug=self.cleaned_data['slug'])
    #
    #     return new_tag


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = ['session_key', 'title', 'products_name', 'nmb']

        exclude = [""]
    # class Meta:
    #     model = Post
    #     fields = ['title', 'slug', 'body', 'image', 'tags']
    #
    #
    #     wighets = {
    #         'title': forms.TextInput(attrs={'class': 'form-control'}),
    #         'slug': forms.TextInput(attrs={'class': 'form-control'}),
    #         'body': forms.Textarea(attrs={'class': 'form-control'}),
    #         'image': forms.FileInput(attrs={'class': 'form-control-file'}),
    #         'tags': forms.SelectMultiple(attrs={'class':'form-control'})


        # }

        def clean_slug(self):
            new_slug = self.cleaned_data['slug'].lower()
            if new_slug == 'create':
                raise ValidationError('Slug may not be "Create"')
            return new_slug



class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductInBasket
        # fields = ['session_key', 'title', 'products_name', 'nmb']

        exclude = [""]
        # wighets = {
        #     'session_key': forms.TextInput(attrs={'class': 'form-control'}),
        #     'title': forms.TextInput(attrs={'class': 'form-control'}),
        #     'products_name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'nmb': forms.Textarea(attrs={'class': 'form-control'}),
        #     'is_active' : forms.BooleanField(default=True)
        #
        #
        # }

        # def clean_slug(self):
        #     new_slug = self.cleaned_data['slug'].lower()
        #     if new_slug == 'create':
        #         raise ValidationError('Slug may not be "Create"')
        #     return new_slug


# class ProductImage(models.Model):
#     session_key = models.CharField(max_length=128, blank=True, null=True, default=None)
#     product = models.ForeignKey(Product, blank=True, null=True, default=None)
#     image = models.ImageField(upload_to='products_images/')
#     is_main = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     created = models.DateTimeField(auto_now_add=True, auto_now=False)
#     updated = models.DateTimeField(auto_now_add=False, auto_now=True)
#
#     def __str__(self):
#         return "%s" % self.id
#
#     class Meta:
#         verbose_name = 'Фотография'
#         verbose_name_plural = 'Фотографии'


