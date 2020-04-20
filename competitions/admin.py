from django.contrib import admin
from .models import Competitions,Question,Submission
# Register your models here.

admin.site.register(Competitions)
admin.site.register(Question)
admin.site.register(Submission)