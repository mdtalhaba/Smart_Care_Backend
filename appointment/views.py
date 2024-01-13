from django.shortcuts import render
from rest_framework import viewsets
from .models import Appointment
from .serializers import AppointmentSerializer

class AppointmentViewsets(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def get_queryset(self) :
        queryset = super().get_queryset()

        patient_id = self.request.query_params.get('patient_id')
        if patient_id :
            queryset = Appointment.objects.filter(patient=patient_id)
        return queryset
