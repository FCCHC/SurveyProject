from django.shortcuts import render

from rest_framework import generics
from rest_framework.views import APIView, Request, Response
from .models import UserData, Country, State,City, Question, Answer, ParentData, SourceInfo, Programs
from .serializers import UserDataSerializer, CountrySerializer, StateSerializer, CitySerializer, \
    QuestionSerializer, AnswerSerializer, ParentDataSerializer, SourceInfoSerializer, ProgramsSerializer
# Create your views here.


class UserDataList(generics.ListCreateAPIView):
    """
    List all user data
    """

    queryset = UserData.objects.all()
    serializer_class = UserDataSerializer

    def get(self, Request):
        if UserData.parent:
            objmodelquery = ParentData.objects.all()
            parentdatarray = list()
            for parent in objmodelquery:
                print(parent.parent)
                parentdatarray.append({
                    "parent": parent.parent,
                    "name": parent.name,
                    "phone": parent.phone,
                    "email": parent.email,
                })
                data = parentdatarray
            return Response(data)
        else:
            return Response(UserData)


class QuestionList(generics.ListCreateAPIView):
    """
    List all questions
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerList(generics.ListCreateAPIView):
    """
    List all answers
    """

    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


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


class ParentList(generics.ListCreateAPIView):
    """
    List parent data
    """
    queryset = ParentData.objects.all()
    serializer_class = ParentDataSerializer


class SourceList(generics.ListCreateAPIView):
    """
    List all sources
    """
    queryset = SourceInfo.objects.all()
    serializer_class = SourceInfoSerializer


class ProgramList(generics.ListCreateAPIView):
    """
    List programs
    """
    queryset = Programs.objects.all()
    serializer_class = ProgramsSerializer



