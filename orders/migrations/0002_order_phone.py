# Generated by Django 3.0.7 on 2020-07-11 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(default='00000000', max_length=12),
        ),
    ]
