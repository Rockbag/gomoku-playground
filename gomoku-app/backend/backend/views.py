from django.http import HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_GET


@require_GET
@ensure_csrf_cookie
def csrf_token(request):
    """Use this endpoint to set the CSRF token in the cookie."""
    return HttpResponse()

