# Generated by Django 4.1.7 on 2023-05-01 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("view_apps", "0026_alter_app_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="app",
            name="id",
            field=models.CharField(
                default="58911722", max_length=1000, primary_key=True, serialize=False
            ),
        ),
    ]
