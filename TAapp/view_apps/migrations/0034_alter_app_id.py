# Generated by Django 4.2.1 on 2023-05-15 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("view_apps", "0033_semester_alter_app_id_course_semester"),
    ]

    operations = [
        migrations.AlterField(
            model_name="app",
            name="id",
            field=models.CharField(
                default="82436765", max_length=1000, primary_key=True, serialize=False
            ),
        ),
    ]
