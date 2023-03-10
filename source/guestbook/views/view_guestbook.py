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


def update_review(request: WSGIRequest, pk):
    review = get_object_or_404(GuestReview, pk=pk)
    if request.method == 'GET':
        form = GuestReviewForm(instance=review)
        return render(request, 'update_review.html', context={'form': form, 'review': review})
    else:
        form = GuestReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, 'update_review.html', context={'form': form})


def delete_review(request: WSGIRequest, pk):
    review = get_object_or_404(GuestReview, pk=pk)
    if request.method == 'GET':
        return render(request, 'review_confirm_delete.html', context={'review': review})
    else:
        review.delete()
        return redirect('home')
