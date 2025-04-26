from django.contrib import admin
from django.urls import path
from todo.views import DeleteTodo, EditTodo, TodoAppView, AddTodo, UpdateTodoItem
from . import views;

urlpatterns = [
    path("admin/", admin.site.urls),  # Admin site
    path("", TodoAppView, name="todolist"),  # View the to-do list
    path("todo/", AddTodo, name="addTodo"),  # Add a to-do item
    path("todo/delete/<int:id>/", views.DeleteTodo, name="deleteTodo"),  # Delete a to-do item
    path("todo/edit/<int:id>/", views.EditTodo, name="editTodo"),  # Edit a to-do item
    path("todo/update/<int:id>/", views.UpdateTodoItem, name="updateTodo"),  # Update a to-do item
]
