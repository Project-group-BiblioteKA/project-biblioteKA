# Generated by Django 4.2 on 2023-05-06 00:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("copies", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="loandbook",
            name="is_return",
            field=models.BooleanField(default=False),
        ),
    ]
