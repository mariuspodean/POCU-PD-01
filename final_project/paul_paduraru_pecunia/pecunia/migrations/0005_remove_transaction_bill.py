# Generated by Django 3.0.8 on 2020-08-03 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pecunia', '0004_transaction_bill'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='bill',
        ),
    ]