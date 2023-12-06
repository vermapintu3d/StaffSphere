from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Test

# Create your views here.

def Home(request):
    return HttpResponse("Welcome to Django")

def practice(request):
    my1 = Test.objects.all().values()
    template = loader.get_template("practice.html")
    context = {
        "my1":my1,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    my2 = Test.objects.get(id=id)
    template = loader.get_template("details.html")
    context = {
        'my2':my2,
    }
    return HttpResponse(template.render(context, request))

def login(request):
    template = loader.get_template("loginpage.html")

    return HttpResponse(template.render())

def signup(request):
    template = loader.get_template("signup.html")

    return HttpResponse(template.render())