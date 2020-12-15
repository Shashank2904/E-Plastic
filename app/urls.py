from django.urls import path,include
from . import views

urlpatterns = [

    path("",views.Index,name="index"),
    path("aboutus/",views.Aboutus,name="aboutus"),
    path("service/",views.Service,name="service"),
    path("news/",views.News,name="news"),
    path("contact/",views.Contact,name="contact"),
    path("registration/",views.Registration,name="registration"),
    path("login/",views.Login,name="login"),

]