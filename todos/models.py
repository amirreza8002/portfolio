from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class TodoList(models.Model):
    title = models.CharField(verbose_name=_("list title"), max_length=100, unique=True)

    def get_absolute_url(self):
        return reverse("todo_list")

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"TodoList({self.title})"


class TodoItem(models.Model):
    title = models.CharField(verbose_name=_("item title"), max_length=100)
    description = models.TextField(verbose_name=_("description"), null=True, blank=True)
    created_date = models.DateTimeField(
        verbose_name=_("created date"), auto_now_add=True
    )
    done = models.BooleanField(verbose_name=_("task is done"), default=False)
    todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse(
            "item-update",
            args=(
                str(self.todo_list.id),
                str(self.id),
            ),
        )

    def __str__(self):
        return f"{self.title} done: {self.done}"

    class Meta:
        ordering = ("created_date", "done")
