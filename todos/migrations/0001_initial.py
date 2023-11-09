# Generated by Django 4.2.7 on 2023-11-09 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TodoList",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        max_length=100, unique=True, verbose_name="list title"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TodoItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100, verbose_name="item title")),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="description"),
                ),
                (
                    "created_date",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="created date"
                    ),
                ),
                (
                    "done",
                    models.BooleanField(default=False, verbose_name="task is done"),
                ),
                (
                    "todo_list",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="todos.todolist"
                    ),
                ),
            ],
            options={
                "ordering": ("created_date", "done"),
            },
        ),
    ]