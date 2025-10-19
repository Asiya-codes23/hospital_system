from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import MedicalRecord, Prescription, LabTest, Invoice
from .serializers import MedicalRecordSerializer, PrescriptionSerializer, LabTestSerializer, InvoiceSerializer

class MedicalRecordViewSet(viewsets.ModelViewSet):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer
    
    @action(detail=False, methods=['get'])
    def by_patient(self, request):
        patient_id = request.query_params.get('patient_id')
        if patient_id:
            records = MedicalRecord.objects.filter(patient_id=patient_id)
            serializer = self.get_serializer(records, many=True)
            return Response(serializer.data)
        return Response({'error': 'patient_id required'}, status=400)

class PrescriptionViewSet(viewsets.ModelViewSet):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
    
    @action(detail=False, methods=['get'])
    def by_patient(self, request):
        patient_id = request.query_params.get('patient_id')
        if patient_id:
            prescriptions = Prescription.objects.filter(patient_id=patient_id)
            serializer = self.get_serializer(prescriptions, many=True)
            return Response(serializer.data)
        return Response({'error': 'patient_id required'}, status=400)

class LabTestViewSet(viewsets.ModelViewSet):
    queryset = LabTest.objects.all()
    serializer_class = LabTestSerializer
    
    @action(detail=False, methods=['get'])
    def pending(self, request):
        tests = LabTest.objects.filter(status='Pending')
        serializer = self.get_serializer(tests, many=True)
        return Response(serializer.data)

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    
    @action(detail=False, methods=['get'])
    def unpaid(self, request):
        invoices = Invoice.objects.filter(payment_status='Unpaid')
        serializer = self.get_serializer(invoices, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def total_revenue(self, request):
        from django.db.models import Sum
        total = Invoice.objects.aggregate(Sum('amount_paid'))['amount_paid__sum'] or 0
        return Response({'total_revenue': total})