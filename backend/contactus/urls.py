from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('newMessage',views.newMessage),
    path('getAllMessages',views.getAllMessages),
    path('deleteMessage',views.deleteMessage),
    
]