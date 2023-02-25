from django.contrib import admin

from guestbook.models import GuestReview


# Register your models here.

class GuestReviewAdmin(admin.ModelAdmin):
    list_display = ('author', 'email', 'description', 'created_at', 'updated_at', 'status')


admin.site.register(GuestReview, GuestReviewAdmin)
