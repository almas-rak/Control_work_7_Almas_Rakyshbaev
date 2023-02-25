from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from guestbook.models import GuestReview


def index_view(request: WSGIRequest):
    reviews = GuestReview.objects.filter(status = 'active')
    return render(request, 'index.html', context={'reviews': reviews} )