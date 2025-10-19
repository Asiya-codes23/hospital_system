from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Doctor
from .serializers import DoctorSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['full_name', 'specialization', 'email', 'phone_number']
    ordering_fields = ['full_name', 'specialization', 'date_joined']
    
    @action(detail=False, methods=['get'])
    def count(self, request):
        count = Doctor.objects.count()
        return Response({'count': count})
    
    @action(detail=False, methods=['get'])
    def available(self, request):
        available_doctors = Doctor.objects.filter(availability='Available')
        serializer = self.get_serializer(available_doctors, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def by_specialization(self, request):
        spec = request.query_params.get('specialization')
        if spec:
            doctors = Doctor.objects.filter(specialization__icontains=spec)
            serializer = self.get_serializer(doctors, many=True)
            return Response(serializer.data)
        return Response([])