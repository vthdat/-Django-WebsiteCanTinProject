# Generated by Django 3.0.7 on 2020-07-16 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Food', '0002_food_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]