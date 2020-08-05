# Generated by Django 3.0.8 on 2020-08-03 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beer_calculator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='ingredient',
            field=models.ManyToManyField(to='beer_calculator.Ingredient'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price for 100 g (RON)'),
        ),
    ]
