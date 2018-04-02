import json

from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseServerError
from django.views.decorators.http import require_POST


@require_POST
def create_user(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    # TODO: better error handling
    try:
        User.objects.create_user(username=username, password=password)
        response = HttpResponse(content=json.dumps({'status': 'ok'}), content_type='application/json')
    except Exception:
        response = HttpResponseServerError(content=json.dumps({'status': 'error',
                                                               'error_message': 'Unexpected error while creating user'}),
                                           content_type='application/json')

    return response

