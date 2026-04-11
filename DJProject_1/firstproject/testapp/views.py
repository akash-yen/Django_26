from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.
def wish(request):
    return render(request, 'testapp/wish.html')