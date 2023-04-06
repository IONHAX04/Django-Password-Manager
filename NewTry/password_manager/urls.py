from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .views import *
from django.http import HttpResponse

urlpatterns = [
    path('', index, name='index'),
    path('mainpage/', mainpage, name='mainpage'),
    path('manage_items', manage_items, name='manage_items'),
    path('delete_items/<int:myid>/', delete_items, name='delete_items'),
    path('update_items/<int:myid>/', update_items, name='update_items'),
    path('updates/<int:myid>/', updates, name='updates'),
]
