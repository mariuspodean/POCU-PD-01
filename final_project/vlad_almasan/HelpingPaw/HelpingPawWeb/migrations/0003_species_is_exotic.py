# Generated by Django 3.0.8 on 2020-07-30 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HelpingPawWeb', '0002_auto_20200730_1744'),
    ]

    operations = [
        migrations.AddField(
            model_name='species',
            name='is_exotic',
            field=models.BooleanField(default=False, verbose_name='Exotic'),
        ),
    ]