from django.shortcuts import render
from django.http import HttpResponse

def about(request):
    return HttpResponse("<h1>About page from secondapp</h1>")

# Create your views here.
