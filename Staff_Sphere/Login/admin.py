from django.contrib import admin
from .views import Test

# Register your models here.

class TestAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "email","mobile_no", "DOB", "gender",)
  
admin.site.register(Test, TestAdmin)