from django.shortcuts import render,redirect
from .models import *
from django.db.models import *
from . import forms
from .forms import Message
# Create your views here.

def home(request):
	top_places = Place.objects.annotate(avg_rate = Avg('rating')).order_by('-avg_rate')[:4]
	return render(request,'base.html',{'top_places': top_places.all() })

def contact(request):
	if request.method == 'POST':
		form = forms.Message(request.POST)
		if form.is_valid():
			form.save()
			return redirect('main:home')
	else:
		form = forms.Message()
	return render(request,'contact.html',{'form':form})

def blog(request):
	# return render(request,'blog.html')
	if request.method == 'POST':
		form = forms.NewsLetterSubscribe(request.POST)
		if form.is_valid():
			form.save()
			return redirect('main:home')
	else:
		form = forms.NewsLetterSubscribe()
	return render(request,'blog.html',{'form':form})

def jaipur(request):
	return render(request,'jaipur.html')

def jaisalmer(request):
	return render(request,'jaisalmer.html')

def jodhpur(request):
	return render(request,'jodhpur.html')