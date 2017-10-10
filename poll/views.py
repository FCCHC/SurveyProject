from django.shortcuts import render

from rest_framework import generics

from .models import UserData,Country,State,City
from .serializers import UserDataSerializer,CountrySerializer,StateSerializer,CitySerializer
# Create your views here.


class UserDataList(generics.ListCreateAPIView):
    """
    List all user data
    """

    queryset = UserData.objects.all()
    serializer_class = UserDataSerializer


class CountryList(generics.ListCreateAPIView):
    """
    List all countrys
    """

    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class StateList(generics.ListCreateAPIView):
    """
    List all states
    """

    queryset = State.objects.all()
    serializer_class = StateSerializer


class CityList(generics.ListCreateAPIView):
    """
    List all cities
    """

    queryset = City.objects.all()
    serializer_class = CitySerializer
