# Generated by Django 3.0.8 on 2020-08-04 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beer_calculator', '0006_auto_20200804_1431'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='add_date',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='add_date',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='quantity',
        ),
    ]
