from django.urls import path
from subject.api.views import SubjectViewSet


urlpatterns = [
    path('create/', SubjectViewSet.as_view({'post': 'create_subject'})),
    path('renew_cookie/', SubjectViewSet.as_view({'post': 'renew_cookie'})),
    path('list_groups/', SubjectViewSet.as_view({'get': 'list_groups'}))
]