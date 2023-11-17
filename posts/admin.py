from django.contrib import admin

from .models import Post
from .forms import PostForm


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostForm
    list_display = ("title", "author", "published_date", "status")
    list_filter = ("status", "created_date", "published_date", "author")
    search_fields = ("title", "body")
    raw_id_fields = ("author",)
    date_hierarchy = "published_date"
    ordering = ("status", "published_date")
