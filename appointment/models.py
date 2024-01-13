from django.db import models
from patient.models import Patient
from doctor.models import Doctor, AvailableTime

APPOINTMENT_STATUS = [
    ('Pending', 'Pending'),
    ('Running', 'Running'),
    ('Completed', 'Completed'),
]
APPOINTMENT_TYPES = [
    ('Online', 'Online'),
    ('Offline', 'Offline'),
]

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_types = models.CharField(choices=APPOINTMENT_TYPES, max_length=10, default='Online')
    appointment_status = models.CharField(choices=APPOINTMENT_STATUS, max_length=10, default='Pending')
    symptom = models.TextField()
    time = models.ForeignKey(AvailableTime, on_delete=models.CASCADE)
    cancel = models.BooleanField(default=False)

    def __str__(self):
        return f"Doctor : {self.doctor.user.first_name} {self.doctor.user.last_name},  Patient : {self.patient.user.first_name}{self.patient.user.last_name}."