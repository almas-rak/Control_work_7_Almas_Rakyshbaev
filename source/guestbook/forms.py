from django import forms

from guestbook.models import GuestReview


class GuestReviewForm(forms.ModelForm):
    class Meta:
        model = GuestReview
        fields = ('author', 'email', 'description')
