from django.utils.deprecation import MiddlewareMixin
from django.utils.functional import SimpleLazyObject
from django.conf import settings
from subject.models import SubjectIdentity


def get_subject(request):
    cookie = request.META.get(settings.COOKIE_HEADER_KEY)
    if not cookie:
        return None
    subject_token = cookie.replace(f"{settings.COOKIE_KEY}=", "")
    try:
        return SubjectIdentity.objects.select_related('subject').get(token=subject_token).subject
    except:
        return None


class SetSubjectMiddleware(MiddlewareMixin):
    def process_request(self, request):
        setattr(request, 'subject', SimpleLazyObject(lambda: get_subject(request)))