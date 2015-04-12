from django.db import models
from django import forms

# Create your models here.
class EmailForm(forms.Form):
      firstname = forms.CharField(max_length=255)
      lastname = forms.CharField(max_length=255)
      email = forms.EmailField()
      subject = forms.CharField(max_length=255)
      botcheck = forms.CharField(max_length=5)
      message = forms.CharField()