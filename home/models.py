from django.db import models

# Create your models here.

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=30)
    content = models.TextField(max_length=500)
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'NAME   - ' + self.name + ' and' + ' EMAIL   - ' + self.email

