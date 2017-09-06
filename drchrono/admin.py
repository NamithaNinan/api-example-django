from django.contrib import admin
from drchrono.models import Patient, User, Appointment

admin.site.register(Patient)
admin.site.register(User)
admin.site.register(Appointment)