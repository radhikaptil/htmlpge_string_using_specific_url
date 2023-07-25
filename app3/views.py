from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sem (request):
    return render(request,'sem.html')
def length(request):
    return render(request,'length.html')
def string3(request):
    return HttpResponse('<h1>This is string3</h1>')