# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
# from apps.endpoints.urls import urlpatterns as endpoints_urlpatterns (wenn endpoints.urls nicht in workaround)

urlpatterns = [
    path('admin/', admin.site.urls),                   # Django admin route
    path("", include("apps.authentication.urls")),     # Auth routes - login / register
    path('quality1/', include("apps.quality1.urls")),   # Route to Quality Parameters
    path('rest/', include("apps.endpoints.urls")),      # workaround für endpoints/urls
    path('django_plotly_dash/', include('django_plotly_dash.urls')),
    path('explainer/', include("apps.explainer.urls")),           #Route for ExplainerDashboard
    # ADD NEW Routes HERE


    # Leave `Home.Urls` as last the last line
    path("", include("apps.home.urls")),         #UI Kits HTML files
]

# urlpatterns += endpoints.urlpatterns