# Generated by Django 4.1.7 on 2023-04-19 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('view_apps', '0015_alter_app_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='id',
            field=models.CharField(default='79856983', max_length=1000, primary_key=True, serialize=False),
        ),
    ]
