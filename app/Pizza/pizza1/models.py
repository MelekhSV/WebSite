from django.db import models
from django.shortcuts import reverse
from  django.utils.text import slugify
# Create your models here.
from time import time






class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150,blank=True, unique=True)
    body = models.TextField(blank=True, db_index=True)
    image = models.ImageField(default=None)
    tags = models.ManyToManyField('Tag',blank=True, related_name='pizzas')
    data_pub = models.DateTimeField(auto_now_add=True)


    def get_absolute_url(self):
        return reverse('pizza_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return '{}'. format(self.title)




class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'slug':self.slug})



    def __str__(self):
        return '{}'.format(self.title)
