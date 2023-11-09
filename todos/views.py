from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin

from .models import TodoItem, TodoList


def todo_list_view(request):
    lists = TodoList.objects.all()
    return render(request, "todos/lists.html", {"lists": lists})


def todo_item_list_view(request, list_id):
    items = TodoItem.objects.filter(todo_list_id=list_id)
    todo_list = TodoList.objects.get(id=list_id)

    return render(
        request, "todos/todo_list.html", {"items": items, "todo_list": todo_list}
    )


class TodoListCreate(UserPassesTestMixin, CreateView):
    model = TodoList
    fields = ("title",)

    def test_func(self):
        return self.request.user.is_authenticated


class TodoItemCreate(UserPassesTestMixin, CreateView):
    model = TodoItem
    fields = (
        "todo_list",
        "title",
        "description",
        "done",
    )

    def get_initial(self):
        initial_data = super().get_initial()
        todo_list = TodoList.objects.get(id=self.kwargs["list_id"])
        initial_data["todo_list"] = todo_list
        return initial_data

    def get_success_url(self):
        return reverse("todo_item_list", args=(self.object.todo_list_id,))

    def test_func(self):
        return self.request.user.is_authenticated


class TodoItemUpdate(UserPassesTestMixin, UpdateView):
    model = TodoItem
    fields = (
        "todo_list",
        "title",
        "description",
        "done",
    )

    def get_success_url(self):
        return reverse("todo_item_list", args=(self.object.todo_list_id,))

    def test_func(self):
        return self.request.user.is_authenticated


class TodoListDelete(UserPassesTestMixin, DeleteView):
    model = TodoList
    success_url = reverse_lazy("todo_list")

    def test_func(self):
        return self.request.user.is_authenticated


class TodoItemDelete(UserPassesTestMixin, DeleteView):
    model = TodoItem

    def get_success_url(self):
        return reverse_lazy("todo_item_list", args=(self.kwargs["list_id"],))

    def test_func(self):
        return self.request.user.is_authenticated
