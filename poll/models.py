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
    school = models.CharField(max_length=500, blank=True)
    parent = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class ParentData(models.Model):
    user = models.ForeignKey(UserData)
    Parent = (
        ('M', 'MAMÁ'),
        ('P', 'PAPÁ'),
    )

    parent = models.CharField(max_length=1, choices=Parent)
    name = models.CharField(max_length=500)
    phone = models.BigIntegerField()
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.parent


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


class SourceInfo(models.Model):
    user = models.ForeignKey(UserData)
    Source = (
        ('RS', 'Redes Sociales'),
        ('W', 'Whatsapp'),
        ('C', 'Correo'),
        ('L', 'Llamada'),
        ('F', 'Folleto'),
    )

    source = models.CharField(max_length=2, choices=Source)

    def __str__(self):
        return self.source


class Programs(models.Model):
    user = models.ForeignKey(UserData)
    Program = (
        ('EV', 'Europa VIP'),
        ('EL', 'Europa Lujo'),
        ('ECH', 'Europa Chic'),
        ('ECHL', 'Europa Chic + Londres'),
        ('OM', 'Orlando & Miami'),
        ('OMH', 'Orlando & Miami+Harmony'),
        ('JCH', 'Japón&China'),
    )

    program = models.CharField(max_length=4, choices=Program)

    def __str__(self):
        return self.program



