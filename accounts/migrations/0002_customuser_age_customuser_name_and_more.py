# Generated by Django 4.2.6 on 2023-11-02 05:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="age",
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="customuser",
            name="name",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Name of user"
            ),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="email",
            field=models.EmailField(
                max_length=254, unique=True, verbose_name="Email address"
            ),
        ),
    ]