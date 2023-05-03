from django.db import models
import uuid


# Create your models here.
class Book(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=50)
    description = models.TextField()
    author = models.CharField(max_length=50)
    amount = models.IntegerField(default=None)
    avaliable = models.IntegerField(null=True, default=0)
