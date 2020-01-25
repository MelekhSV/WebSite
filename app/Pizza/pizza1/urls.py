from django.urls import path
from .views import *

urlpatterns = [
    path('', Project_Function, name='project_list_url'),
    path('result/', Result_Function, name='result_list_url')