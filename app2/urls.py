from django.urls import path
from app2.views import *

app_name='name'

urlpatterns=[
    path('pop/',pop,name='pop'),
    path('total/',total,name='total'),
    path('string2/',string2,name='string2'),

]