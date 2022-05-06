from django.shortcuts import render


# Create your views here.
def blog(request):
    return render(request, 'blog.html')

def home(request):
    return render(request, 'home.html')

def say_hello(request):
    return render(request, 'hello.html')
