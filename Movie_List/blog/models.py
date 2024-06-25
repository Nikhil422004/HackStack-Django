from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=35)
    director = models.CharField(max_length=35)
    releaseDate = models.DateField()
    genre = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title