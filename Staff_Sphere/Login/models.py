from django.db import models
from django import forms

# Create your models here.

class Test(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  email = models.CharField(max_length=255, null=True)
  mobile_no = models.IntegerField(null=True)
  DOB = models.DateField(null=True)
  gender = models.CharField(max_length=1, null=True)


  def __str__(self):
    return f"{self.firstname} {self.lastname}"
  

  
class LoginForm(forms.Form):
  username = forms.CharField(max_length=100, required=True, help_text="Enter your username")
  password = forms.CharField(max_length=100, required=True, help_text="Enter your password")