# Generated by Django 4.2.2 on 2023-07-20 04:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_alter_movie_world_premiere'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='world_premiere',
            field=models.DateField(default=datetime.date(2023, 7, 20), verbose_name='Примьеры в мире'),
        ),
    ]
