from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="physical-home"),
    path('sleep/', views.sleep, name="physical-sleep"),
    path('exercise/', views.exercise, name="physical-exercise"),
]
