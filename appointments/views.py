from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Appointment
from .serializers import AppointmentSerializer
from datetime import datetime, timedelta

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['patient__full_name', 'doctor__full_name', 'status']
    ordering_fields = ['date', 'time']
    
    @action(detail=False, methods=['get'])
    def count(self, request):
        count = Appointment.objects.count()
        return Response({'count': count})
    
    @action(detail=False, methods=['get'])
    def recent(self, request):
        recent = Appointment.objects.all().order_by('-date_created')[:10]
        serializer = self.get_serializer(recent, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def today(self, request):
        today = datetime.now().date()
        today_appointments = Appointment.objects.filter(date=today)
        serializer = self.get_serializer(today_appointments, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def upcoming(self, request):
        today = datetime.now().date()
        upcoming = Appointment.objects.filter(date__gte=today, status='Scheduled').order_by('date', 'time')
        serializer = self.get_serializer(upcoming, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def by_date_range(self, request):
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')
        
        if start_date and end_date:
            appointments = Appointment.objects.filter(date__range=[start_date, end_date])
            serializer = self.get_serializer(appointments, many=True)
            return Response(serializer.data)
        return Response({'error': 'start_date and end_date required'}, status=400)
    
    @action(detail=False, methods=['get'])
    def by_status(self, request):
        status = request.query_params.get('status')
        if status:
            appointments = Appointment.objects.filter(status=status)
            serializer = self.get_serializer(appointments, many=True)
            return Response(serializer.data)
        return Response([])
