from django.urls import path
from psycho_test.api.question.views import QuestionViewSet
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('list/', csrf_exempt(QuestionViewSet.as_view({'get': 'list'}))),
]