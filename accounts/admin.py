from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'phone_number', 'date_created')
    list_filter = ('role',)
    search_fields = ('user__username', 'user__email', 'phone_number')

admin.site.register(UserProfile, UserProfileAdmin)
