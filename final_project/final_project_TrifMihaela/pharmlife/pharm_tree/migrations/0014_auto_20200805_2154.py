# Generated by Django 3.0.8 on 2020-08-05 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharm_tree', '0013_auto_20200804_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drugs',
            name='name_of_drug',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='pacient',
            name='name_pacient',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
