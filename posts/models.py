from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField(max_length=100000)
    class Gender(models.Choices):
        MAN =  "MAN"
        WOMAN =  "WOMAN"
        # (...)
    gender = models.CharField(max_length=999999999999999,choices=Gender.choices,default=Gender.MAN)

    image = models.ImageField(upload_to='posts/',default='default.png')
    author = models.ForeignKey(User,related_name='post_author',on_delete=models.CASCADE)

    tags = TaggableManager()




    def __str__(self):
        return self.title