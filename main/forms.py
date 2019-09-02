from django import forms
from . import models
# from .models import GetInTouch

class Message(forms.ModelForm):
	class Meta:
		model=models.SendMessage
		fields = ['message','name','subject','email']#required fields(input by user)

class NewsLetterSubscribe(forms.ModelForm):
	class Meta:
		model = models.NewsLetter
		fields = ['email']