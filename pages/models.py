from django.db import models
from django.utils.translation import gettext_lazy as _


class RepositoryMetadata(models.Model):
    """Information about one of repos fetched from the GitHub API."""

    last_updated = models.DateTimeField(
        help_text=_("The date and time this data was last fetched"),
        auto_now=True,
    )
    repo_name = models.CharField(
        primary_key=True,
        max_length=40,
        help_text=_("the full name of the repo, e.g. amirreza8002/portfolio"),
    )
    description = models.CharField(
        max_length=400,
        help_text=_("the description of the repo.")
    )
    forks = models.IntegerField(
        help_text=_("the number of forks of this repo"),
    )
    stargazers = models.IntegerField(
        help_text=_("The number of stargazers for this repo"),
    )
    language = models.CharField(
        max_length=20,
        help_text=_("the primary programming language used for this repo."),
    )

    def __str__(self):
        return self.repo_name
