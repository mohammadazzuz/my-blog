# Generated by Django 4.1.5 on 2023-01-25 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
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
                ("title", models.CharField(max_length=20)),
                ("content", models.TextField(max_length=200)),
                (
                    "gender",
                    models.CharField(
                        choices=[("1", "MAN"), ("2", "WOMAN")],
                        default="1",
                        max_length=2,
                    ),
                ),
            ],
        ),
    ]
