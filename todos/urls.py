from django.urls import path

from .views import (
    todo_list_view,
    todo_item_list_view,
    TodoListDelete,
    TodoItemDelete,
    TodoItemUpdate,
    TodoItemCreate,
    TodoListCreate,
)


urlpatterns = [
    path("", todo_list_view, name="todo_list"),
    path("list/<int:list_id>/", todo_item_list_view, name="todo_item_list"),
    path("list/add/", TodoListCreate.as_view(), name="list_add"),
    path("list/<int:pk>/delete/", TodoListDelete.as_view(), name="list_delete"),
    path("items/<int:list_id>/add/", TodoItemCreate.as_view(), name="item_add"),
    path(
        "items/<int:list_id>/update/<int:pk>/",
        TodoItemUpdate.as_view(),
        name="item_update",
    ),
    path(
        "items/<int:list_id>/delete/<int:pk>/",
        TodoItemDelete.as_view(),
        name="item_delete",
    ),
]
