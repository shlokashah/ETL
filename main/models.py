from django.db import models

# Create your models here.
'''
TODO: 
fix Place class to show appropriate places and images
make comments visible for each tour, make template for each tour
fix newsletter and sendmessage
'''
class Place(models.Model):
    main_place = models.CharField(max_length=100)
    sub_place = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images/", default="/static/img/logo.png")
    cost = models.IntegerField(default=0)
    description = models.TextField(max_length=1000, blank=False, default="Awesome place!")

class Rating(models.Model):
    place_visited = models.ForeignKey(Place,on_delete=models.CASCADE)
    username = models.TextField(max_length=30, default="Anonymous")
    comment = models.TextField(default="This was an awesome place!!", max_length=300)
    rate = models.IntegerField(default=5)

class SendMessage(models.Model):
	message = models.TextField(default="Enter Message")
	name= models.TextField(default="Enter Your Name")
	subject = models.CharField(max_length=50)
	email = models.EmailField(max_length=254)

class NewsLetter(models.Model):
    email = models.EmailField(max_length=254)