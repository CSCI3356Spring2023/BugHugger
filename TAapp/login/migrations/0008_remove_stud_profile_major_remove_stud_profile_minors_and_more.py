# Generated by Django 4.1.7 on 2023-04-19 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_delete_admin_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stud_profile',
            name='major',
        ),
        migrations.RemoveField(
            model_name='stud_profile',
            name='minors',
        ),
        migrations.AddField(
            model_name='stud_profile',
            name='CS_major',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='stud_profile',
            name='currently_hired',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='stud_profile',
            name='year',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]
