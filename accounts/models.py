from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    name = models.CharField(_("Name of user"), max_length=255)
    email = models.EmailField(_("Email address"), unique=True)
    age = models.PositiveSmallIntegerField(null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
