from django.urls import path
from .views import *

urlpatterns = [
    path('', pizza_list, name='pizza_list_url'),
    path('pizza/<str:slug>/', PostDetail.as_view(), name='pizza_detail_url'),
    path('tags/', tags_list, name='tags_list_url'),
    path('tag/<str:slug>/', TagDetail.as_view(), name='tag_detail_url')
]