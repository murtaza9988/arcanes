# Generated by Django 4.1.5 on 2023-02-16 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_ev_margin1_profile_ev_margin2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='ev_margin1_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='ev_margin2_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='ev_margin3_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='ev_won_count',
            field=models.IntegerField(default=0),
        ),
    ]