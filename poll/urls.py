from django.conf.urls import include, url
from django.contrib import admin

from .views import *

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    url(r'^UserData', UserDataList.as_view()),
    url(r'^countryList/$', CountryList.as_view()),
    url(r'^stateList/$', StateList.as_view()),
    url(r'^cityList/$', CityList.as_view()),
    url(r'^questionList/$', QuestionList.as_view()),
    url(r'^answerList/$', AnswerList.as_view()),
]
