from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import Test, LoginForm

# Create your views here.

def Main(request):
    template = loader.get_template("Main.html")
    return HttpResponse(template.render())

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

def loginUser(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data(['uname'])
            password = form.cleaned_data(['password'])
            userData = Test.objects.filter({username:username, password:password })
            if(userData):
                context = {
                  'my3':userData[0],
                }
            else:
                return HttpResponseRedirect('/signup.html')
        template = loader.get_template("userinfo.html")
        return HttpResponse(template.render(context, request))
    
    else : 
        form = LoginForm()

    return render(request, 'loginpage.html', {form: form})