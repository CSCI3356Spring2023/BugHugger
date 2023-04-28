# Generated by Django 4.1.7 on 2023-04-28 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('view_apps', '0019_app_is_visible_alter_app_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='num_assigned',
            field=models.IntegerField(blank=True, default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name='app',
            name='id',
            field=models.CharField(default='95999217', max_length=1000, primary_key=True, serialize=False),
        ),
    ]
