from django.urls import path
from django.http import HttpResponse
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('encode', views.encode, name='encode'),
    path('decode', views.decode, name='decode'),
]