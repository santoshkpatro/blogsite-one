from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    sno  = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    content = models.TextField()
    author = models.CharField(max_length=30)
    timeStamp = models.DateTimeField(blank=True)

    def __str__(self):
        return self.title + ' by ' + self.author

