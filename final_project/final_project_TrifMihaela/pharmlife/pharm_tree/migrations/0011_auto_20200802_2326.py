# Generated by Django 3.0.8 on 2020-08-02 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharm_tree', '0010_auto_20200802_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drugs',
            name='data_of_expiration',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='date_of_renew',
            field=models.DateField(),
        ),
    ]
