# Generated by Django 4.1.7 on 2023-04-28 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('view_apps', '0018_alter_app_id_alter_course_assigned_students'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='is_visible',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='app',
            name='id',
            field=models.CharField(default='46075617', max_length=1000, primary_key=True, serialize=False),
        ),
    ]
