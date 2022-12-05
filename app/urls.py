from django.urls import path
from django.http import HttpResponse
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('encode', views.encode, name='encode'),
    path('decode', views.decode, name='decode'),
    path('view', views.view, name='view'),
    path('delete', views.delete, name='delete'),
]