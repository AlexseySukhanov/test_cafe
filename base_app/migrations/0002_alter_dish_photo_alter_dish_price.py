# Generated by Django 4.0 on 2021-12-15 12:42

import base_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='photo',
            field=models.ImageField(blank=True, upload_to=base_app.models.Dish.get_file_name),
        ),
        migrations.AlterField(
            model_name='dish',
            name='price',
            field=models.FloatField(),
        ),
    ]
