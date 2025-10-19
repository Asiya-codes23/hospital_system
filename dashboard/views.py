from django.shortcuts import render
from patients.models import Patient
from doctors.models import Doctor
from appointments.models import Appointment
from medical_records.models import MedicalRecord, Prescription, LabTest, Invoice
from django.db.models import Count, Sum
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    # Basic counts
    total_patients = Patient.objects.count()
    total_doctors = Doctor.objects.count()
    total_appointments = Appointment.objects.count()
    completed_appointments = Appointment.objects.filter(status='Completed').count()
    scheduled_appointments = Appointment.objects.filter(status='Scheduled').count()
    cancelled_appointments = Appointment.objects.filter(status='Cancelled').count()
    
    # Available doctors
    available_doctors = Doctor.objects.filter(availability='Available').count()
    
    # Medical records stats
    total_medical_records = MedicalRecord.objects.count()
    total_prescriptions = Prescription.objects.count()
    pending_lab_tests = LabTest.objects.filter(status='Pending').count()
    
    # Financial stats
    total_invoices = Invoice.objects.count()
    unpaid_invoices = Invoice.objects.filter(payment_status='Unpaid').count()
    total_revenue = Invoice.objects.aggregate(Sum('amount_paid'))['amount_paid__sum'] or 0
    pending_revenue = Invoice.objects.filter(payment_status='Unpaid').aggregate(Sum('amount'))['amount__sum'] or 0
    
    # Recent data
    recent_appointments = Appointment.objects.all().order_by('-date_created')[:10]
    recent_medical_records = MedicalRecord.objects.all()[:5]
    recent_prescriptions = Prescription.objects.all()[:5]
    pending_tests = LabTest.objects.filter(status='Pending')[:5]
    
    # Today's data
    today = datetime.now().date()
    today_appointments = Appointment.objects.filter(date=today)
    
    # Charts data
    appointments_by_status = {
        'scheduled': scheduled_appointments,
        'completed': completed_appointments,
        'cancelled': cancelled_appointments,
    }
    
    doctors_by_specialization = Doctor.objects.values('specialization').annotate(count=Count('id'))
    
    context = {
        'total_patients': total_patients,
        'total_doctors': total_doctors,
        'total_appointments': total_appointments,
        'completed_appointments': completed_appointments,
        'scheduled_appointments': scheduled_appointments,
        'cancelled_appointments': cancelled_appointments,
        'available_doctors': available_doctors,
        'total_medical_records': total_medical_records,
        'total_prescriptions': total_prescriptions,
        'pending_lab_tests': pending_lab_tests,
        'total_invoices': total_invoices,
        'unpaid_invoices': unpaid_invoices,
        'total_revenue': total_revenue,
        'pending_revenue': pending_revenue,
        'recent_appointments': recent_appointments,
        'recent_medical_records': recent_medical_records,
        'recent_prescriptions': recent_prescriptions,
        'pending_tests': pending_tests,
        'today_appointments': today_appointments,
        'appointments_by_status': appointments_by_status,
        'doctors_by_specialization': doctors_by_specialization,
    }

    return render(request, 'dashboard/home.html', context)

def api_docs(request):
    return render(request, 'dashboard/api_docs.html')