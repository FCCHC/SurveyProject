from rest_framework import serializers

from .models import UserData,Country,State,City


class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = ('name', 'gender', 'age', 'date_of_birth', 'phone', 'email')


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('name', 'country')


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ('name', 'state')


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('name', 'city')
