from django.db import models

# Create your models here.


class UserData (models.Model):
    name = models.CharField(max_length=500)
    Gender = (
        ('F', 'Femenino'),
        ('M', 'Masculino'),
    )

    gender = models.CharField(max_length=1, choices=Gender)
    age = models.PositiveIntegerField()
    date_of_birth = models.DateField()
    phone = models.BigIntegerField()
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.name


class Question(models.Model):
    user = models.ForeignKey(UserData)
    question = models.CharField(max_length=500)

    def __str__(self):
        return self.question


class Answer(models.Model):
    question = models.ForeignKey(Question)
    answer = models.CharField(max_length=500)

    def __str__(self):
        return self.answer


class Country(models.Model):
    user = models.ForeignKey(UserData)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.country


class State(models.Model):
    country = models.ForeignKey(Country)
    state = models.CharField(max_length=100)

    def __str__(self):
        return self.state


class City(models.Model):
    state = models.ForeignKey(State)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.city
