from django.contrib import admin
from .models import UserData, Question, Answer
# Register your models here.

admin.site.register(UserData)
admin.site.register(Question)
admin.site.register(Answer)


