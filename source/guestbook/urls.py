from django.urls import path

from guestbook.views.view_guestbook import index_view

urlpatterns = [
    path('', index_view),
]
