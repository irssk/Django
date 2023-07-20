from TodoApp import views
from django.urls import path



urlpatterns = [
    path("todoList", views.todoList, name="todoList"),
    path("description", views.description_page, name="description")
]





