from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from psycho_test.api.answer.views import AnswerViewSet


urlpatterns = [
    path('set/', csrf_exempt(AnswerViewSet.as_view({'post': 'set_answer'}))),
]