from django.db import models

class Personality(models.Model):
    personality_type = models.CharField('Personality Type', max_length=50)
    description = models.CharField(max_length=5000)

    def __str__(self):
        return self.personality_type

class Species(models.Model):
    name = models.CharField('Name', max_length=100)
    is_exotic = models.BooleanField('Exotic', default=False)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField('Name', max_length=50)

    def __str__(self):
        return self.name

class Shelter(models.Model):
    name = models.CharField('Name', max_length=200)
    city = models.ForeignKey(City, on_delete=models.PROTECT)
    address = models.CharField('Address', max_length=500)
    capacity = models.PositiveIntegerField('Capacity', default=0)
    picture = models.ImageField('Picture', upload_to='images', null=True)

    def __str__(self):
        return f'Name: {self.name}, Address: {self.address}'


class Animal(models.Model):
    name = models.CharField('Name', max_length=100)
    age = models.PositiveIntegerField('Years Old', default=0)
    picture = models.ImageField('Picture', upload_to='images', null=True)
    description = models.CharField('Description', max_length=2000)
    adopted = models.BooleanField('Adopted', default=False)
    adopted_date = models.DateField('Adopted Date', blank=True, null=True)
    reserved = models.BooleanField('Reserved', default=False)
    personality_type = models.ForeignKey(Personality, on_delete=models.PROTECT)
    species = models.ForeignKey(Species, on_delete=models.PROTECT)
    shelter = models.ForeignKey(Shelter, on_delete=models.PROTECT)

    def __str__(self):
        return f'Species: {self.species} Name: {self.name}'


class Partner(models.Model):
    name = models.CharField('Name', max_length=1000)
    date_joined = models.DateField('Date Joined')
    contribution = models.CharField('Contribution', max_length=5000)
    shelter_contributed_to = models.ForeignKey(Shelter, on_delete=models.PROTECT)
    picture = models.ImageField('Picture', upload_to='images', null=True)

    def __str__(self):
        return self.name

class Reservation(models.Model):
    first_name = models.CharField('First Name', max_length=50)
    last_name = models.CharField('Last Name', max_length=50)
    email = models.EmailField('Email', max_length=100)
    reserved_date = models.DateTimeField('Reservation Date')
    reserved_animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    reserved_shelter = models.ForeignKey(Shelter, on_delete=models.CASCADE)

    def __str__(self):
        return f'First Name: {self.first_name} Last Name: {self.last_name}, Date: {self.reserved_date}, Animal: {self.reserved_animal.name}'
