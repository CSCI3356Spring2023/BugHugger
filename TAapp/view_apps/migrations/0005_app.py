# Generated by Django 4.1.7 on 2023-03-22 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("view_apps", "0004_course_section"),
    ]

    operations = [
        migrations.CreateModel(
            name="App",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("course_id", models.CharField(max_length=15)),
                ("student_name", models.CharField(max_length=100)),
                ("eagle_id", models.CharField(max_length=15)),
                ("office_hours", models.CharField(max_length=10)),
                ("major", models.CharField(max_length=200)),
                ("why_ta", models.CharField(max_length=500)),
            ],
        ),
    ]
