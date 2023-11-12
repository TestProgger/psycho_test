from django.urls import path, include

urlpatterns = [
    path('test/', include('psycho_test.api.psycho_test.urls')),
    path('question/', include('psycho_test.api.question.urls')),
    path('answer/', include('psycho_test.api.answer.urls'))
]