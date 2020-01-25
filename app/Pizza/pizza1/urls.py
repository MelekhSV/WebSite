from django.urls import path
from .views import *

urlpatterns = [
    path('', Project_Function, name='pizza_list_url'),
    path('pizza/<str:slug>/', pizza_detail, name='pizza_detail_url'),
    path('tags/', tags_list, name='tags_list_url'),
    path('tag/<str:slug>/', tag_detail, name='tag_detail_url')
]