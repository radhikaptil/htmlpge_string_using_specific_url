from django.urls import path
from app3.views import *

app_name='day'

urlpatterns=[
    path('sem/',sem,name='sem'),
    path('length/',length,name='length'),
    path('string3/',string3,name='string3'),
]