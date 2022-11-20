from django.urls import path
from . import views
from .dash_apps.finished_apps import simpleexample     # Für django_plotly_dash integration

urlpatterns = [
    path('', views.explainer,name="explainerdashboard"),
]