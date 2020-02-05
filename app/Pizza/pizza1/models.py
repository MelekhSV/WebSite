from django.db import models
from django.shortcuts import reverse
from  django.utils.text import slugify
# Create your models here.
from time import time

from django.utils.text import slugify


def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))





class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150,blank=True, unique=True)
    body = models.TextField(blank=True, db_index=True)
    image = models.ImageField(blank=True,default=None)
    tags = models.ManyToManyField('Tag',blank=True, related_name='pizzas')
    data_pub = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def get_absolute_url(self):
        return reverse('pizza_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('pizza_update_url', kwargs={'slug': self.slug})


    def __str__(self):
        return self.title

    #
    # генерация слага по title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)


    class Meta:
        ordering = ['-data_pub']



class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'slug':self.slug})


    def get_update_url(self):
        return reverse('tag_update_url', kwargs={'slug': self.slug})

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        ordering = ['-title']

class ProductInBasket(models.Model):


    session_key = models.CharField(max_length=128, blank=True, null=True, default=None)
    title = models.CharField(max_length=128, blank=True, null=True, default=None)
    products_name = models.CharField(max_length=150, db_index=True)
    # slug = models.SlugField(max_length=150,blank=True, unique=True)
    # body = models.TextField(blank=True, db_index=True)
    nmb = models.IntegerField(default=1)
    products_price = models.DecimalField(max_digits=10, decimal_places=2, default=1)
    is_active = models.BooleanField(default=True)

    # image = models.ImageField(blank=True,default=None)
    # tags = models.ManyToManyField('Tag',blank=True, related_name='pizzas')
    # data_pub = models.DateTimeField(auto_now_add=True)


    # def get_absolute_url(self):
    #     return reverse('pizza_detail_url', kwargs={'slug': self.slug})
    #
    # def get_update_url(self):
    #     return reverse('pizza_update_url', kwargs={'slug': self.slug})


    # def __str__(self):
    #     return self.products_name

    #
    # генерация слага по title

    # def save(self, *args, **kwargs):
    #     if not self.id:
    #         self.slug = gen_slug(self.title)
    #     super().save(*args, **kwargs)


    # class Meta:
    #
    #     verbose_name = 'ssss'
    #     verbose_name_price = 'dddd'


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