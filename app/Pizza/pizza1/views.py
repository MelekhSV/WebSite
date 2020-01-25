from django.shortcuts import render

# Create your views here.
from .models import Post



def Project_Function(request):
    pizza = Post.objects.all()
    return render(request, 'Pizza/index.html', context={'pizza':pizza})

def Result_Function(request):
    return render(request, 'Django/result.html')