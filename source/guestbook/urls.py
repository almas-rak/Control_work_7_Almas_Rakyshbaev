from django.urls import path

from guestbook.views.view_guestbook import create_review, index_view

urlpatterns = [
    path('', index_view, name='home'),
    path('add/review', create_review, name='create_review')
]
