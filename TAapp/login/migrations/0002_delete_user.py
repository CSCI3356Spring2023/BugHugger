# Generated by Django 4.1.7 on 2023-03-22 04:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("login", "0001_initial"),
    ]

    operations = [
        migrations.DeleteModel(
            name="User",
        ),
    ]