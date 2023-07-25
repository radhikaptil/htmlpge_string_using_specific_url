from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def page(request):
    return render(request,'page.html')
def remain(request):
    return render(request,'remain.html')
def string1(request):
    return HttpResponse('<h1>This is string1</h1>')