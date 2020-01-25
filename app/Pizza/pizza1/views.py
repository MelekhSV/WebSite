from django.shortcuts import render

# Create your views here.



def Project_Function(request):
    return render(request, 'Pizza/index.html')

def Result_Function(request):
    return render(request, 'Django/result.html')