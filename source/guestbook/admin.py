from django.contrib import admin

from guestbook.models import GuestReview


# Register your models here.

class GuestReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'email', 'description', 'status', 'created_at', 'updated_at',)
    list_editable = ('author', 'email', 'description', 'status')


admin.site.register(GuestReview, GuestReviewAdmin)
