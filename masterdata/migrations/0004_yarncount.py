# Generated by Django 5.0.6 on 2024-09-23 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("masterdata", "0003_unit"),
    ]

    operations = [
        migrations.CreateModel(
            name="YarnCount",
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
                ("yarn_count", models.CharField(max_length=120)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
