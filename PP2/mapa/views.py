from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'html/home.html')

def teste(request):
    return render (request, 'html/teste.html')