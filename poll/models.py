from django.db import models

# Create your models here.


class UserData (models.Model):
    name = models.CharField(max_length=100)
    Gender = (
        ('F', 'Femenino'),
        ('M', 'Masculino'),
    )

    gender = models.CharField(max_length=1, choices=Gender)
    age = models.PositiveIntegerField()
    date_of_birth = models.DateField()
    phone = models.PositiveIntegerField()
    email = models.EmailField(max_length=254)


class Country(models.Model):
    name = models.ForeignKey(UserData)
    country = models.CharField(max_length=100)


class State(models.Model):
    name = models.ForeignKey(Country)
    state = models.CharField(max_length=100)


class City(models.Model):
    name = models.ForeignKey(State)
    city = models.CharField(max_length=100)
