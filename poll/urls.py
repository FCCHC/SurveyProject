from django.conf.urls import include, url
from django.contrib import admin

from survey.poll import views

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    url(r'^poll/$', views.CountryList.as_view()),
]
