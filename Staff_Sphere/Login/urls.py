from django.urls import path
from .import views

urlpatterns = [
    path('', views.Main, name = 'Main'),
    path('login/', views.login, name="loginpage"),
    path('signup/', views.signup, name="signup"),
    path('practice/',views.practice, name='practice'),
    path('practice/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
    ]