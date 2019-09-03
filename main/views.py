from django.shortcuts import render,redirect
from .models import *
from django.db.models import *
from . import forms
from validate_email import validate_email
from .forms import Message
from django.http import HttpResponse
# Create your views here.

def home(request):
    top_places = Place.objects.annotate(avg_rate=Avg('rating')).order_by('-avg_rate')[:4]
    if request.method == "POST":
        mail = request.POST["email"]
        if validate_email(mail):
            newsletter = NewsLetter()
            newsletter.email=mail
            newsletter.save()
        else:
            top_places = Place.objects.annotate(avg_rate=Avg('rating')).order_by('-avg_rate')[:4]
            return render(request, 'base.html', {'top_places': top_places.all(), "warning":"Must be a valid email"})
    else:
        top_places = Place.objects.annotate(avg_rate = Avg('rating')).order_by('-avg_rate')[:4]
    return render(request,'base.html',{'top_places': top_places.all() })

def contact(request):
    if request.method == "POST":
        new_contact = SendMessage()
        name = request.POST["name"].strip()
        message = request.POST["message"].strip()
        email = request.POST['email'].strip()
        subject = request.POST['subject'].strip()
        if  validate_email(email):
            new_contact.name = name
            new_contact.message = message
            new_contact.email = email
            new_contact.subject = subject
            new_contact.save()
            return redirect("main:contact")
        else:
            return redirect("main:home")
    else:
        return render(request, 'contact.html')

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

def place(request, slug):
    slug_places = Place.objects.filter(sub_place__contains=slug)
    if len(list(slug_places.all())) < 1:
        return redirect("main:home")
    reviews = Rating.objects.filter(place_visited__sub_place__contains=slug)
    return render(request, "place.html", {"places":slug_places.all(), "reviews":reviews.all()})

def top(request):
    top_places = Place.objects.annotate(avg_rate=Avg('rating')).order_by('-avg_rate')
    return render(request, "order.html", {"places":top_places})

def gallery(request):
    return render(request,'gallery.html')

def packages(request):
    places = Place.objects.all()
    return render(request,"package.html",{'places':places})