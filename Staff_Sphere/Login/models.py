from django.db import models

# Create your models here.

class Test(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  email = models.CharField(max_length=255, null=True)
  mobile_no = models.IntegerField(null=True)
  DOB = models.DateField(null=True)
  gender = models.CharField(max_length=1, null=True)

