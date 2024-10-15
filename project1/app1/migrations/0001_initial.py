# Generated by Django 5.0.4 on 2024-10-12 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="clients",
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
                ("client", models.CharField(max_length=50)),
                ("address", models.CharField(max_length=100)),
                ("zip", models.IntegerField()),
            ],
        ),
    ]
