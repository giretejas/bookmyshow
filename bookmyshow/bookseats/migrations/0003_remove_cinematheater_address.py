# Generated by Django 4.0.6 on 2022-10-11 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookseats', '0002_cinematheater_shows_bookings'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cinematheater',
            name='address',
        ),
    ]
