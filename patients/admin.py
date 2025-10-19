from django.contrib import admin
from .models import Patient

class PatientAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'age', 'gender', 'phone_number', 'date_registered')
    list_filter = ('gender', 'date_registered')
    search_fields = ('full_name', 'phone_number', 'address')
    ordering = ('-date_registered',)

admin.site.register(Patient, PatientAdmin)




