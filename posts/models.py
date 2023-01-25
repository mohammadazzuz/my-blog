from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField(max_length=200)
    class Gender(models.Choices):
        MAN =  "MAN"
        WOM =  "WOMAN"
        # (...)

    gender = models.CharField(
        max_length=999999999999999,
        choices=Gender.choices,
        default=Gender.MAN
    )