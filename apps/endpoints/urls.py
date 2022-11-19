from django.conf.urls import url, include
from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.endpoints.views import EndpointViewSet
from apps.endpoints.views import MLAlgorithmViewSet
from apps.endpoints.views import MLAlgorithmStatusViewSet
from apps.endpoints.views import MLRequestViewSet
from apps.endpoints.views import PredictView # import PredictView

router = DefaultRouter(trailing_slash=False)
router.register(r"endpoints", EndpointViewSet, basename="endpoints")
router.register(r"mlalgorithms", MLAlgorithmViewSet, basename="mlalgorithms")
router.register(r"mlalgorithmstatuses", MLAlgorithmStatusViewSet, basename="mlalgorithmstatuses")
router.register(r"mlrequests", MLRequestViewSet, basename="mlrequests")

urlpatterns = [
    path('api/v1/', include(router.urls)),

    #add predict url
path('api/v1/income_classifier/predict', PredictView.as_view(), name="predict"
),


]
''' 
Der eigentliche URL Code, hat bei mir aber nicht funktioniert, deswegen workaround von oben

urlpatterns = [
    url(r"^api/v1/", include(router.urls)),
    # add predict url
    url(
        r"^api/v1/(?P<endpoint_name>.+)/predict$", PredictView.as_view(), name="predict"
    ),
]

'''

'''
The above code will create REST API routers to our database models. 
Our models will be accessed by following the URL pattern:
http://<server-ip>/rest/api/v1/<object-name>

v1 in the API address might be needed later for API versioning.

'''

