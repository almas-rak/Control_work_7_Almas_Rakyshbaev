from django.urls import path

from guestbook.views.view_guestbook import create_review, index_view, update_review

urlpatterns = [
    path('', index_view, name='home'),
    path('add/review/', create_review, name='create_review'),
    path('update/review/<int:pk>', update_review, name='update_review'),
]
