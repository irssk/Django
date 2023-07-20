from django.contrib import admin
from django.urls import path, include
from TodoApp.urls import urlpatterns
from django.http import HttpResponse




def home(request):
    return HttpResponse("<a href='todoList'>START</a>")




urlpatterns = [
    path('', home),
    path('', include(urlpatterns)),
    path('description', include(urlpatterns)),
]
