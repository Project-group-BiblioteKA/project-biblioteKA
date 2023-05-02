# Generated by Django 4.2 on 2023-05-02 17:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0001_initial"),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="BookFollower",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "books",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="book_follow",
                        to="books.book",
                    ),
                ),
                (
                    "users",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_follower",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="user",
            name="books",
            field=models.ManyToManyField(
                related_name="book_followers",
                through="users.BookFollower",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
