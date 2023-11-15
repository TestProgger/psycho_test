from django.urls import path
from psycho_test.api.psycho_test.views import PsychoTestViewSet
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('list/', csrf_exempt(PsychoTestViewSet.as_view({'get': 'list'}))),
    path('start/', csrf_exempt(PsychoTestViewSet.as_view({'post': 'start_test'}))),
    path('end/', csrf_exempt(PsychoTestViewSet.as_view({'post': 'end_test'}))),
]