# Generated by Django 4.1.13 on 2024-12-16 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PigeonInterrupt",
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
                ("Time", models.DateTimeField()),
                ("PIRSensor", models.BooleanField(default=False)),
                ("CameraSensor", models.BooleanField(default=False)),
            ],
        ),
    ]
