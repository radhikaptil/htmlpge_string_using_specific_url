from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def pop(request):
    return render(request,'pop.html')
def total(request):
    return render(request,'total.html')
def string2(request):
    return HttpResponse('<h1>This is string2</h1>')