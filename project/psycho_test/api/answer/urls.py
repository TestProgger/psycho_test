from django.urls import path
from psycho_test.api.answer.views import AnswerViewSet


urlpatterns = [
    path('set/', AnswerViewSet.as_view({'post': 'set_answer'})),
]