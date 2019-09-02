from django.urls import path
from . import views

app_name="main"

urlpatterns=[
	path('' , views.home , name="home"),
	path('contact/',views.contact,name="contact"),
	path('blog/',views.blog,name="blog"),
	path('jaipur/',views.jaipur,name="jaipur"),
	path('jaisalmer/',views.jaisalmer,name="jaisalmer"),
	path('jodhpur/',views.jodhpur,name="jodhpur")
]
