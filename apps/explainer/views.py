from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def explainer(requests):
    return render(requests,'home/page-ExplainerDashboard.html')