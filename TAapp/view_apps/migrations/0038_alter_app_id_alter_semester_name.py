# Generated by Django 4.2.1 on 2023-05-15 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("view_apps", "0037_alter_app_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="app",
            name="id",
            field=models.CharField(
                default="97857572", max_length=1000, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="semester",
            name="name",
            field=models.CharField(max_length=12, primary_key=True, serialize=False),
        ),
    ]