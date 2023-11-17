from django.contrib import admin

from .models import RepositoryMetadata


@admin.register(RepositoryMetadata)
class RepositoryMetadataAdmin(admin.ModelAdmin):
    pass
