# Generated by Django 4.1.5 on 2023-01-25 04:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("posts", "0006_post_tags_alter_post_gender_alter_post_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="author",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="post_author",
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="post",
            name="gender",
            field=models.CharField(
                choices=[("MAN", "Man"), ("WOMAN", "Woman")],
                default="MAN",
                max_length=999999999999999,
            ),
        ),
    ]
