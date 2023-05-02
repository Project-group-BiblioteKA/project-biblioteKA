from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, max_length=150)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_blocked = models.BooleanField(default=False)

    books = models.ManyToManyField(
        "users.User",
        through="users.BookFollower",
        related_name="book_followers",
    )


class BookFollower(models.Model):
    books = models.ForeignKey(
        "books.Book",
        on_delete=models.CASCADE,
        related_name="book_follow",
    )
    users = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="user_follower"
    )
