from django.core.management.base import BaseCommand
from patients.models import Patient
from doctors.models import Doctor
from appointments.models import Appointment
from medical_records.models import MedicalRecord, Prescription, LabTest, Invoice
from datetime import datetime, timedelta
import random

class Command(BaseCommand):
    help = 'Populate database with sample data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Creating sample data...')
        
        # Create Patients
        patients = []
        for i in range(1, 11):
            patient = Patient.objects.create(
                full_name=f'Patient {i}',
                age=random.randint(18, 80),
                gender=random.choice(['Male', 'Female']),
                phone_number=f'0712345{i:03d}',
                address=f'{i} Main Street, Nairobi'
            )
            patients.append(patient)
        
        self.stdout.write(self.style.SUCCESS(f'Created {len(patients)} patients'))
        
        # Create Doctors
        specializations = ['Cardiology', 'Pediatrics', 'Neurology', 'Orthopedics', 'Dermatology']
        doctors = []
        for i in range(1, 6):
            doctor = Doctor.objects.create(
                full_name=f'Dr. {chr(64+i)} Smith',
                specialization=specializations[i-1],
                phone_number=f'0798765{i:03d}',
                email=f'doctor{i}@hospital.com',
                availability=random.choice(['Available', 'Available', 'Unavailable'])
            )
            doctors.append(doctor)
        
        self.stdout.write(self.style.SUCCESS(f'Created {len(doctors)} doctors'))
        
        # Create Appointments
        statuses = ['Scheduled', 'Completed', 'Cancelled']
        for i in range(20):
            Appointment.objects.create(
                patient=random.choice(patients),
                doctor=random.choice(doctors),
                date=datetime.now().date() + timedelta(days=random.randint(-30, 30)),
                time=datetime.now().time(),
                status=random.choice(statuses),
                notes=f'Appointment notes {i}'
            )
        
        self.stdout.write(self.style.SUCCESS('Created 20 appointments'))
        
        # Create Medical Records
        for i in range(15):
            MedicalRecord.objects.create(
                patient=random.choice(patients),
                doctor=random.choice(doctors),
                diagnosis=f'Diagnosis {i}',
                symptoms=f'Symptoms for patient {i}',
                treatment=f'Treatment plan {i}',
                notes=f'Additional notes {i}'
            )
        
        self.stdout.write(self.style.SUCCESS('Created 15 medical records'))
        
        # Create Prescriptions
        medications = ['Amoxicillin', 'Paracetamol', 'Ibuprofen', 'Metformin', 'Aspirin']
        for i in range(20):
            records = list(MedicalRecord.objects.all())
            if records:
                record = random.choice(records)
                Prescription.objects.create(
                    medical_record=record,
                    patient=record.patient,
                    doctor=record.doctor,
                    medication_name=random.choice(medications),
                    dosage=f'{random.choice([250, 500, 1000])}mg',
                    frequency=random.choice(['Once daily', 'Twice daily', 'Three times daily']),
                    duration=f'{random.randint(5, 30)} days',
                    instructions='Take with food'
                )
        
        self.stdout.write(self.style.SUCCESS('Created 20 prescriptions'))
        
        # Create Lab Tests
        test_types = ['Blood Test', 'X-Ray', 'MRI', 'CT Scan', 'Ultrasound']
        for i in range(10):
            LabTest.objects.create(
                patient=random.choice(patients),
                doctor=random.choice(doctors),
                test_name=random.choice(test_types),
                test_type=random.choice(test_types),
                status=random.choice(['Pending', 'In Progress', 'Completed']),
                description=f'Test description {i}'
            )
        
        self.stdout.write(self.style.SUCCESS('Created 10 lab tests'))
        
        # Create Invoices
        for i in range(10):
            amount = random.uniform(1000, 50000)
            paid = random.uniform(0, amount)
            Invoice.objects.create(
                patient=random.choice(patients),
                invoice_number=f'INV-2025-{i:04d}',
                description=f'Medical services - consultation and tests',
                amount=round(amount, 2),
                amount_paid=round(paid, 2),
                payment_status='Paid' if paid >= amount else 'Unpaid' if paid == 0 else 'Partial',
                due_date=datetime.now().date() + timedelta(days=30)
            )
        
        self.stdout.write(self.style.SUCCESS('Created 10 invoices'))
        self.stdout.write(self.style.SUCCESS('✅ Database populated successfully!'))