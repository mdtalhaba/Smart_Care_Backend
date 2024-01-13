from django.urls import path, include
from rest_framework import routers
from .views import AppointmentViewsets

router = routers.DefaultRouter()

router.register('',AppointmentViewsets)

urlpatterns = [
    path('', include(router.urls))
]
