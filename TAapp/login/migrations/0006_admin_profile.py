# Generated by Django 4.1.7 on 2023-04-10 18:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('login', '0005_alter_prof_profile_department_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin_profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=60)),
                ('last_name', models.CharField(blank=True, max_length=60)),
                ('department', models.CharField(blank=True, max_length=60)),
                ('email', models.EmailField(blank=True, max_length=60)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
