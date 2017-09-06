from django.db import models

from datetime import datetime

# Create your models here.


class Patient(models.Model):
    first_name = models.CharField(default="",max_length=20);
    last_name = models.CharField(default="",max_length=20);
    doctor = models.PositiveIntegerField(default=-1);
    gender = models.CharField(default="Male",max_length=60);
    date_of_birth = models.CharField(default=str(datetime.now()), max_length= 10);


# python manage.py makemigrations
# python manage.py migrate

class User(models.Model):
    user_name = models.CharField(max_length=20);
    access_token = models.CharField(max_length=100);

class Appointment(models.Model):
    patient = models.PositiveIntegerField(default=-1);
    status = models.CharField(default="",max_length=20);
    scheduled_time = models.DateTimeField(blank=True,default=datetime.now());
    duration = models.PositiveIntegerField(default=0);
    dr_seeing = models.BooleanField(default=False)
    dr_seeing_time = models.DateTimeField(null=True, blank=True)
    
    