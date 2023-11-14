from django.utils.deprecation import MiddlewareMixin
from django.utils.functional import SimpleLazyObject
from django.conf import settings
from subject.models import SubjectIdentity, Subject


def get_subject(request):
    try:
        return Subject.objects.get(
            subjectidentity__token=request.COOKIES.get(settings.COOKIE_KEY),
            subjectidentity__secret=request.headers.get(settings.SECRET_HEADER)
        )
    except Exception as ex:
        pass

    return None


class SetSubjectMiddleware(MiddlewareMixin):
    def process_request(self, request):
        setattr(request, 'subject', SimpleLazyObject(lambda: get_subject(request)))