# Generated by Django 3.0.8 on 2020-08-04 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beer_calculator', '0005_auto_20200804_1421'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='ingredient',
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredient',
            field=models.ManyToManyField(to='beer_calculator.Ingredient'),
        ),
    ]
