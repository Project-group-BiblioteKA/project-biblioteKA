from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    author = models.CharField(max_length=50)
    amount = models.IntegerField(default=None)
    avaliable = models.IntegerField(null=True, default=0)