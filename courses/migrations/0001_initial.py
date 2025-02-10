# Generated by Django 5.1.6 on 2025-02-10 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Course",
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
                ("created_at", models.DateTimeField(auto_created=True, auto_now=True)),
                ("name", models.CharField(max_length=50)),
                ("description", models.TextField()),
                ("level", models.CharField(max_length=80)),
                ("schedule", models.TextField()),
                ("duration_course", models.TextField()),
                ("quantity_persons", models.CharField(max_length=15)),
                ("price", models.TextField()),
                ("initial_date", models.DateTimeField()),
                ("final_date", models.DateTimeField()),
                ("registration_deadline", models.DateTimeField()),
                ("goal", models.TextField()),
            ],
        ),
    ]
