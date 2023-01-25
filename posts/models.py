from django.db import models
from taggit.managers import TaggableManager

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField(max_length=200)
    class Gender(models.Choices):
        MAN =  "MAN"
        WOMAN =  "WOMAN"
        # (...)

    gender = models.CharField(
        max_length=999999999999999,
        choices=Gender.choices,
        default=Gender.MAN
    )
    image = models.ImageField(upload_to='posts/',default='default.png')

    tags = TaggableManager()




    def __str__(self):
        return self.title