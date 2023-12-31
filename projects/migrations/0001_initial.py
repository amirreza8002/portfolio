# Generated by Django 4.2.7 on 2023-11-11 18:09

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="RepositoryMetadata",
            fields=[
                (
                    "last_updated",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="The date and time this data was last fetched",
                    ),
                ),
                (
                    "repo_name",
                    models.CharField(
                        help_text="the full name of the repo, e.g. amirreza8002/projects",
                        max_length=40,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "description",
                    models.CharField(
                        help_text="the description of the repo.", max_length=400
                    ),
                ),
                (
                    "forks",
                    models.IntegerField(help_text="the number of forks of this repo"),
                ),
                (
                    "stargazers",
                    models.IntegerField(
                        help_text="The number of stargazers for this repo"
                    ),
                ),
                (
                    "language",
                    models.CharField(
                        help_text="the primary programming language used for this repo.",
                        max_length=20,
                    ),
                ),
            ],
        ),
    ]
