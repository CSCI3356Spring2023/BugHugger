# Generated by Django 4.1.7 on 2023-04-19 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('view_apps', '0012_remove_app_app_id_alter_app_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='id',
            field=models.UUIDField(default='235603', editable=False, primary_key=True, serialize=False),
        ),
    ]
