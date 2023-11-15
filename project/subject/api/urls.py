from django.urls import path
from subject.api.views import SubjectViewSet, LogoutSubjectViewSet
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('create/', csrf_exempt(SubjectViewSet.as_view({'post': 'create_subject'}))),
    path('renew_cookie/', csrf_exempt(SubjectViewSet.as_view({'post': 'renew_cookie'}))),
    path('list_groups/', csrf_exempt(SubjectViewSet.as_view({'get': 'list_groups'}))),
    path('logout/', csrf_exempt(LogoutSubjectViewSet.as_view({'post': 'logout'})))
]