from django.contrib import admin
from .models import Doctor

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'specialization', 'phone_number', 'email', 'availability', 'date_joined')
    list_filter = ('specialization', 'availability')
    search_fields = ('full_name', 'phone_number', 'email')
    ordering = ('-date_joined',)

admin.site.register(Doctor, DoctorAdmin)

