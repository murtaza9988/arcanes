# Generated by Django 4.2.5 on 2023-11-18 20:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("predict", "0018_alter_game_gamedate_retrain"),
    ]

    operations = [
        migrations.CreateModel(
            name="ModelReset",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "date_posted",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("ip", models.CharField(blank=True, max_length=50, null=True)),
                ("model", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]