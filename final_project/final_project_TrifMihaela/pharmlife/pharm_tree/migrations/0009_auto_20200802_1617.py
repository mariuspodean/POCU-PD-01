# Generated by Django 3.0.8 on 2020-08-02 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pharm_tree', '0008_auto_20200802_1308'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='email_address_pacient',
            new_name='name_pacient_recipe',
        ),
    ]
