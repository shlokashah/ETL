from django.urls import path
from . import views

app_name="main"

urlpatterns=[
	path('' , views.home , name="home"),
	path('contact/',views.contact,name="contact"),
	path('blog/',views.blog,name="blog"),
	path('gallery/',views.gallery,name="gallery"),
	path('top_places/',views.top,name="top"),
	path('place/<slug>/', views.place, name="place"),
	path('packages/',views.packages,name="packages"),
]
