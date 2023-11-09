from django.contrib import admin

from .models import TodoList, TodoItem


@admin.register(TodoList)
class TodoListAdmin(admin.ModelAdmin):
    pass


@admin.register(TodoItem)
class TodoItemAdmin(admin.ModelAdmin):
    pass
