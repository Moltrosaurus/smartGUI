from django.urls import path
from . import views

urlpatterns = [
    path('', views.q1, name="q1"),

]
