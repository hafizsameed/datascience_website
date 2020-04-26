
from django import forms
from django.contrib.auth.models import User
from .models import Submission



class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['file']

