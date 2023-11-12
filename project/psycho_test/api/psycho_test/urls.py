from django.urls import path
from psycho_test.api.psycho_test.views import PsychoTestViewSet


urlpatterns = [
    path('list/', PsychoTestViewSet.as_view({'get': 'list'})),
    path('start/', PsychoTestViewSet.as_view({'post': 'start_test'})),
    path('end/', PsychoTestViewSet.as_view({'post': 'end_test'})),
]