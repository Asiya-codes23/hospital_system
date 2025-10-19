from django.contrib import admin
from .models import MedicalRecord, Prescription, LabTest, Invoice

class PrescriptionInline(admin.TabularInline):
    model = Prescription
    extra = 1

class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'diagnosis', 'date_created')
    list_filter = ('date_created', 'doctor')
    search_fields = ('patient__full_name', 'diagnosis', 'symptoms')
    inlines = [PrescriptionInline]
    ordering = ('-date_created',)

class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'medication_name', 'dosage', 'date_prescribed')
    list_filter = ('date_prescribed', 'doctor')
    search_fields = ('patient__full_name', 'medication_name')
    ordering = ('-date_prescribed',)

class LabTestAdmin(admin.ModelAdmin):
    list_display = ('patient', 'test_name', 'status', 'date_ordered', 'date_completed')
    list_filter = ('status', 'date_ordered')
    search_fields = ('patient__full_name', 'test_name')
    ordering = ('-date_ordered',)

class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('invoice_number', 'patient', 'amount', 'amount_paid', 'payment_status', 'due_date')
    list_filter = ('payment_status', 'date_issued')
    search_fields = ('invoice_number', 'patient__full_name')
    ordering = ('-date_issued',)

admin.site.register(MedicalRecord, MedicalRecordAdmin)
admin.site.register(Prescription, PrescriptionAdmin)
admin.site.register(LabTest, LabTestAdmin)
admin.site.register(Invoice, InvoiceAdmin)
