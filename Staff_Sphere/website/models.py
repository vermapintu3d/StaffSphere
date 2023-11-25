from django.db import models

# Create your models here

class Login(models.Model):
    Username = models.EmailField(max_length=30)
    Password = models.CharField(max_length=255)
