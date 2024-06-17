from django.contrib import admin
from django.urls import path

from django import views
from . import views

urlpatterns = [
    path('index',views.index,name='index'),
    path('sebas',views.sebas,name='sebas'),
    path('kevin',views.kevin,name='kevin')
]