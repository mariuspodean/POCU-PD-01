# Generated by Django 3.0.8 on 2020-07-29 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharm_tree', '0005_auto_20200729_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drugs',
            name='data_of_expiration',
            field=models.DateTimeField(verbose_name='date_expiration'),
        ),
    ]
