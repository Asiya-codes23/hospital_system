from django.contrib import admin
from .models import Appointment

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'date', 'time', 'status', 'date_created')
    list_filter = ('status', 'date', 'doctor')
    search_fields = ('patient__full_name', 'doctor__full_name')
    ordering = ('-date_created',)

admin.site.register(Appointment, AppointmentAdmin)

