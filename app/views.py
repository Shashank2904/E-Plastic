from django.shortcuts import render

# Create your views here.

def Index(request):
    return render(request,"app/index.html")

def Aboutus(request):
    return render(request,"app/about.html")

def Service(request):
    return render(request,"app/service.html")

def News(request):
    return render(request,"app/blog.html")   

def Contact(request):
    return render(request,"app/contact.html")   

def Registration(request):
    return render(request,"app/registration.html")

def Login(request):
    return render(request,"app/login.html")
