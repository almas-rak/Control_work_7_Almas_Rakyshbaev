from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404

from guestbook.forms import GuestReviewForm
from guestbook.models import GuestReview


def index_view(request: WSGIRequest):
    reviews = GuestReview.objects.filter(status='active')
    return render(request, 'index.html', context={'reviews': reviews})


def create_review(request: WSGIRequest):
    if request.method == 'GET':
        form = GuestReviewForm()
        return render(request, 'create_review.html', context={'form': form})
    else:
        form = GuestReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, 'create_review.html', context={'form': form})
