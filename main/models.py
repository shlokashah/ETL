from django.db import models

# Create your models here.

class Place(models.Model):
    main_place = models.CharField(max_length=100)
    sub_place = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images/", default="/static/img/logo.png")

class Rating(models.Model):
    # user = blah blah blah!
    place_visited = models.ForeignKey(Place,on_delete=models.CASCADE)
    comment = models.TextField(default="This was an awesome place!!")
    rate = models.IntegerField(default=5)

class SendMessage(models.Model):
	message = models.TextField(default="Enter Message")
	name= models.TextField(default="Enter Your Name")
	subject = models.CharField(max_length=50)
	email = models.EmailField(max_length=254)

class NewsLetter(models.Model):
    email = models.EmailField(max_length=254)