
from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Patient
from .serializers import PatientSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['full_name', 'email', 'phone_number', 'medical_id']
    ordering_fields = ['full_name', 'date_registered']
    
    @action(detail=False, methods=['get'])
    def count(self, request):
        count = Patient.objects.count()
        return Response({'count': count})
    
    @action(detail=False, methods=['get'])
    def search(self, request):
        query = request.query_params.get('q', '')
        if query:
            patients = Patient.objects.filter(full_name__icontains=query)
            serializer = self.get_serializer(patients, many=True)
            return Response(serializer.data)
        return Response([])

