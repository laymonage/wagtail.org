# Generated by Django 3.2.18 on 2023-04-26 00:23

import django.db.models.deletion
from django.db import migrations, models

import modelcluster.fields


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Milestone",
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
                ("publish", models.BooleanField(default=True)),
                (
                    "number",
                    models.IntegerField(
                        editable=False, help_text="GitHub milestone number", unique=True
                    ),
                ),
                (
                    "state",
                    models.CharField(
                        choices=[("OPEN", "Open"), ("CLOSED", "Closed")],
                        editable=False,
                        max_length=32,
                    ),
                ),
                ("due_on", models.DateField(blank=True, editable=False, null=True)),
                ("title", models.CharField(max_length=255)),
                ("url", models.URLField(verbose_name="URL")),
            ],
            options={
                "verbose_name": "roadmap milestone",
                "verbose_name_plural": "roadmap milestones",
                "ordering": ["-due_on"],
            },
        ),
        migrations.CreateModel(
            name="Item",
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
                ("publish", models.BooleanField(default=True)),
                (
                    "needs_sponsorship",
                    models.BooleanField(default=False, editable=False),
                ),
                (
                    "number",
                    models.IntegerField(
                        editable=False, help_text="GitHub issue number", unique=True
                    ),
                ),
                (
                    "state",
                    models.CharField(
                        choices=[("OPEN", "Open"), ("CLOSED", "Closed")],
                        editable=False,
                        max_length=32,
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("url", models.URLField(verbose_name="URL")),
                (
                    "labels",
                    models.TextField(
                        blank=True, help_text="Comma-separated list of labels"
                    ),
                ),
                (
                    "milestone",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items",
                        to="roadmap.milestone",
                    ),
                ),
            ],
            options={
                "verbose_name": "roadmap item",
                "verbose_name_plural": "roadmap items",
            },
        ),
    ]
