from rest_framework import serializers
from .models import Appointment

class AppointmentSerializer(serializers.ModelSerializer) :
    # patient = serializers.StringRelatedField()
    # doctor = serializers.StringRelatedField()
    # time = serializers.StringRelatedField()
    class Meta:
        model = Appointment
        fields = '__all__'