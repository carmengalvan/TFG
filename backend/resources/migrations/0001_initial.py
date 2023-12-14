# Generated by Django 4.2.8 on 2023-12-13 18:29

import datetime
import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Resource",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True, null=True, verbose_name="created date"
                    ),
                ),
                (
                    "modified",
                    models.DateTimeField(
                        auto_now=True, null=True, verbose_name="modified date"
                    ),
                ),
                ("name", models.CharField(max_length=30, verbose_name="name")),
                (
                    "description",
                    models.CharField(max_length=100, verbose_name="description"),
                ),
                (
                    "available_time",
                    models.TimeField(
                        help_text="Time resource is available for reservation",
                        verbose_name="available_time",
                    ),
                ),
                (
                    "start_date",
                    models.DateField(
                        default=datetime.date.today, verbose_name="start_date"
                    ),
                ),
                ("end_date", models.DateField(verbose_name="end_date")),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="user",
                    ),
                ),
            ],
            options={
                "verbose_name": "resource",
                "verbose_name_plural": "resources",
                "ordering": ["start_date"],
            },
        ),
        migrations.CreateModel(
            name="DayAvailability",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True, null=True, verbose_name="created date"
                    ),
                ),
                (
                    "modified",
                    models.DateTimeField(
                        auto_now=True, null=True, verbose_name="modified date"
                    ),
                ),
                ("day", models.DateField(verbose_name="day")),
                ("start_time", models.TimeField(verbose_name="start_time")),
                ("end_time", models.TimeField(verbose_name="end_time")),
                (
                    "resource",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="resources.resource",
                        verbose_name="resource",
                    ),
                ),
            ],
            options={
                "verbose_name": "availability",
                "verbose_name_plural": "availabilities",
                "ordering": ["day"],
            },
        ),
    ]
