from django.urls import path
from app1.views import *

app_name='book'

urlpatterns=[
    path('page/',page,name='page'),
    path('remain/',remain,name='remain'),
    path('string1/',string1,name='string1'),
]
