from django.shortcuts import render
from .models import Todo


# Create your views here.
def blog(request):
    return render(request, 'blog.html')

def home(request):
    all = Todo.objects.all()
    return render(request, 'home.html', {'todos': all})

def say_hello(request):
    person = {'name': 'admin'}
    return render(request, 'hello.html', context=person)
