from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.



def practice(request):
    template = loader.get_template("practice.html")
 
    return HttpResponse(template.render(context, request))

def login(request):
    template = loader.get_template("loginpage.html")

    return HttpResponse(template.render())

def signup(request):
    template = loader.get_template("signup.html")

    return HttpResponse(template.render())