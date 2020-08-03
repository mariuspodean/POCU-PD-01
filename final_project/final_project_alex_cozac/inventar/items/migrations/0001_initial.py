# Generated by Django 3.0.8 on 2020-08-02 20:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('distributors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=250)),
                ('quantity', models.IntegerField()),
                ('distributor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='distributors.Distributor')),
            ],
        ),
    ]
