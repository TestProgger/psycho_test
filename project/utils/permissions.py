from rest_framework import permissions


class IsSubjectSet(permissions.BasePermission):
    def has_permission(self, request, view):
        print(request.subject)
        return bool(request.subject)