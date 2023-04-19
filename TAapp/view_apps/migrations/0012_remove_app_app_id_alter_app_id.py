# Generated by Django 4.1.7 on 2023-04-19 20:33

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('view_apps', '0011_app_app_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='app',
            name='app_id',
        ),
        migrations.AlterField(
            model_name='app',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
