# Generated by Django 4.2 on 2023-05-03 13:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("title", models.CharField(max_length=50)),
                ("description", models.TextField()),
                ("author", models.CharField(max_length=50)),
                ("amount", models.IntegerField(default=None)),
                ("avaliable", models.IntegerField(default=0, null=True)),
            ],
        ),
    ]
