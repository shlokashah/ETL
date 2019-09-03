from django.urls import path
from . import views

app_name="main"

urlpatterns=[
	path('' , views.home , name="home"),
	path('contact/',views.contact,name="contact"),
	path('blog/',views.blog,name="blog"),
	path('gallery/',views.gallery,name="gallery"),
	path('place/', views.all_places, name="all_places"),
	path('place/<slug>/', views.place, name="place")
]
