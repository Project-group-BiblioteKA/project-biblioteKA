# Generated by Django 4.2 on 2023-05-08 13:07

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="book",
            old_name="description",
            new_name="synopse",
        ),
    ]
