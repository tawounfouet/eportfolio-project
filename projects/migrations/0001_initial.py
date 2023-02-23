# Generated by Django 4.1.6 on 2023-02-14 13:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Project",
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
                ("name", models.CharField(max_length=100)),
                ("summary", models.CharField(max_length=500)),
                (
                    "field",
                    models.CharField(
                        choices=[
                            ("ML", "Machine Learning"),
                            ("DL", "Deep Learning"),
                            ("DS", "Data Science"),
                        ],
                        max_length=5,
                    ),
                ),
                (
                    "description",
                    models.TextField(blank=True, verbose_name="Description"),
                ),
                (
                    "year_created",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(1900),
                            django.core.validators.MaxValueValidator(2021),
                        ]
                    ),
                ),
                ("active", models.BooleanField(default=True)),
            ],
        ),
    ]
