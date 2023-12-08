from django.contrib.sitemaps import Sitemap

from .models import TodoList, TodoItem


class TodoListSitemap(Sitemap):
    changefreq = "monthly"

    def items(self):
        return TodoList.objects.all()


class TodoItemSitemap(Sitemap):
    changefreq = "weekly"

    def items(self):
        return TodoItem.objects.all()

    def lastmod(self, obj):
        return obj.created_date
