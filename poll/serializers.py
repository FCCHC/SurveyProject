from rest_framework import serializers

from .models import UserData, Country, State, City, Question, Answer, ParentData, SourceInfo, Programs


class ParentDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParentData
        fields = ("parent", "name", "phone", "email")


class UserDataSerializer(serializers.ModelSerializer):
    Data = ParentDataSerializer()

    class Meta:
        model = UserData
        fields = "__all__"


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = "__all__"


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"


class SourceInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SourceInfo
        fields = "__all__"


class ProgramsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programs
        fields = "__all__"
