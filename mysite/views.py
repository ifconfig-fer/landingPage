from django.shortcuts import render
from django.http import HttpResponse

def hello_world(request):
    return render(request, 'hello_world.html')

def about(request):
    return render(request, 'about.html')

def legal(request):
    return render(request, 'legal.html')