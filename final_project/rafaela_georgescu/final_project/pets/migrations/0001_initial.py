# Generated by Django 3.0.8 on 2020-08-02 10:45

import datetime
from django.db import migrations, models
import django.db.models.deletion
import pets.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('size', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], max_length=1)),
                ('gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male')], max_length=1)),
                ('description', models.TextField(blank=True)),
                ('date_added', models.DateTimeField(default=datetime.datetime.now)),
                ('main_photo', models.ImageField(upload_to=pets.models.pet_directory_path)),
                ('photo_1', models.ImageField(blank=True, upload_to=pets.models.pet_directory_path)),
                ('photo_2', models.ImageField(blank=True, upload_to=pets.models.pet_directory_path)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Owner')),
            ],
        ),
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('pet_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pets.Pet')),
                ('breed', models.CharField(blank=True, max_length=200)),
                ('special_needs', models.TextField(blank=True)),
                ('is_neutered', models.BooleanField(default=False)),
                ('is_vaccinated', models.BooleanField(default=False)),
                ('is_friendly_with_dogs', models.BooleanField(default=False)),
                ('is_friendly_with_cats', models.BooleanField(default=False)),
                ('is_friendly_with_kids', models.BooleanField(default=False)),
                ('is_microchipped', models.BooleanField(default=False)),
            ],
            bases=('pets.pet',),
        ),
    ]
