import json

from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.utils.safestring import mark_safe


def index(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name='chat/index.html')


@login_required
def room(request: HttpRequest, room_name: str) -> HttpResponse:
    return render(
        request=request,
        template_name='chat/room.html',
        context={
            'room_name_json': mark_safe(json.dumps(room_name)),
            'username': mark_safe(json.dumps(request.user.username))
        }
    )
