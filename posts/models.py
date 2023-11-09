from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from autoslug import AutoSlugField
from taggit.managers import TaggableManager


class PublishedManage(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = "DF", "Draft"
        PUBLISHED = "PB", "Published"

    class Meta:
        ordering = ["-published_date"]
        indexes = [models.Index(fields=["-published_date"])]

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_("author")
    )
    title = models.CharField(verbose_name=_("title"), max_length=255)
    slug = AutoSlugField(verbose_name=_("slug"), populate_from="title", unique=True)
    body = models.TextField(verbose_name=_("body"))
    status = models.CharField(
        max_length=10, choices=Status.choices, default=Status.DRAFT
    )

    created_date = models.DateTimeField(
        verbose_name=_("created date"), auto_now_add=True
    )
    published_date = models.DateTimeField(
        verbose_name=_("published date"), default=timezone.now
    )
    updated_date = models.DateTimeField(verbose_name=_("updated date"), auto_now=True)

    objects = models.Manager()
    published = PublishedManage()
    tags = TaggableManager(verbose_name=_("tags"))

    def __str__(self):
        return self.title
