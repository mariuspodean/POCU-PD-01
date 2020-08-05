# Generated by Django 3.0.8 on 2020-08-04 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('beer_calculator', '0004_auto_20200803_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='quantity',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Quantity (g)'),
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='ingredient',
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredient',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.PROTECT, to='beer_calculator.Ingredient'),
            preserve_default=False,
        ),
    ]
