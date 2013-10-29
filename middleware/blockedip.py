
from django.conf import settings
from django import http


class BlockedIpMiddleware(object):
    """Simple middlware to block IP addresses via settings variable BLOCKED_IPS

    via https://djangosnippets.org/snippets/744/
    """

    def process_request(self, request):
        if request.META.get('REMOTE_ADDR') in getattr(settings, 'BLOCKED_IPS', []) or []:
            return http.HttpResponseForbidden('<h1>Forbidden</h1>')
        return None
