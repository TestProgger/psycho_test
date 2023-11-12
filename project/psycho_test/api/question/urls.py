from django.urls import path
from psycho_test.api.question.views import QuestionViewSet


urlpatterns = [
    path('list/', QuestionViewSet.as_view({'get': 'list'})),
]