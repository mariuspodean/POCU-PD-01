# Generated by Django 3.0.8 on 2020-08-03 15:09

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pecunia', '0003_auto_20200802_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='bill',
            field=models.FileField(default='', storage=django.core.files.storage.FileSystemStorage(location=''), upload_to='bills'),
        ),
    ]
