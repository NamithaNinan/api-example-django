# Create your views here.
import requests
import settings
import refreshtoken
from datetime import datetime
from drchrono.models import Patient, User, Appointment
from django.template import Context
from django.http import HttpResponse
from django.core.mail import send_mail
from django.shortcuts import render,redirect
from django.template.loader import get_template
from django.views.generic.base import TemplateView
from django.views.decorators.csrf import csrf_protect, csrf_exempt
patientsrecords = dict()


def get_token(request):
    template_name = "home.html"

    if (settings.ACCESS_TOKEN == None ):
        settings.oauth_code = request.GET.get('code');
        response = requests.post('https://drchrono.com/o/token/', data={
            'code': settings.oauth_code,
            'grant_type': 'authorization_code',
            'redirect_uri': settings.LOGIN_REDIRECT_URL,
            'client_id': settings.SOCIAL_AUTH_DRCHRONO_KEY,
            'client_secret': settings.SOCIAL_AUTH_DRCHRONO_SECRET,
        })
        data = response.json()
        settings.ACCESS_TOKEN = data['access_token']
        settings.REFRESH_TOKEN = data['refresh_token']
        settings.EXPIRES_IN = data['expires_in']
        refreshtoken.countdown_refresh_accesstoken(settings.EXPIRES_IN)
    data = getcurrentuserinfo()
    username = data['username']
    doc_id = data['doctor']
    appointments = getappointments(doc_id)
    template = get_template(template_name)
    context = {'currentuser': username,"doctors_data":appointments}
    html = template.render(Context(context))
    return HttpResponse(html)
    
def authorisedoc(request):
    link = "https://drchrono.com/o/authorize/?redirect_uri="+settings.LOGIN_REDIRECT_URL+"&response_type=code&client_id="+settings.SOCIAL_AUTH_DRCHRONO_KEY;
    context = {'currentuser': 'Anonymous user','authorizelink':link};
    template_name = "index.html"
    template = get_template(template_name)
    html = template.render(Context(context))
    return HttpResponse(html)


def getappointments(doc_id):
    appointmentslist = []
    appointments = []
    appointments_url = 'https://drchrono.com/api/appointments?date=%s&doctor=%d' % (datetime.now().strftime("%Y-%m-%d"),  doc_id)
    #appointments_url = 'https://drchrono.com/api/appointments/:%d' % doc_id
    while appointments_url:
        data = requests.get(appointments_url, headers={ 'Authorization': 'Bearer %s' % settings.ACCESS_TOKEN,}).json()
        appointmentslist = data['results']
        for each_appointment in appointmentslist:
            if not each_appointment['status'] == None:
                appointments.append(each_appointment)
        appointments_url = data['next']
        
    patients_today = []
    patient_status = {}
    app = []
    
    for appointment in appointments:
        patients_today.append(appointment['patient'])
        app = []
        app.append(appointment['status'])
        app.append(appointment['scheduled_time'])
        app.append(appointment['duration'])
        patient_status[appointment['patient']] = app #appointment['status']
      
    names = []
    patients = []
    patient_url = 'https://drchrono.com/api/patients'
    while patient_url:
        data = requests.get(patient_url, headers={ 'Authorization': 'Bearer %s' % settings.ACCESS_TOKEN,}).json()
        patients.extend(data['results'])
        patient_url = data['next']
        
    total_patients_today = {}
    for patient in patients:
        for key,value in patient_status.items():
            if patient['id'] == key:
                total_patients_today[patient['id']] = value
#        if patient['id'] in patients_today:
#            total_patients_today.append(patient)
    print total_patients_today
    
    for key,value in total_patients_today.items():
        result = []
        print "\n"
        print key
        print "\n"
        result.append(key)
        result.append(value)
        result.append(patientnames(key))
        names.append(result)
        app = Appointment(patient=key, status=value[0], scheduled_time = value[1],duration = value[2])
        app.save()
    print names
    
    return names



def patientnames(patient_id):
    names = []
    patients = []
    name_url = 'https://drchrono.com/api/patients'
    while name_url:
        data = requests.get(name_url, headers={ 'Authorization': 'Bearer %s' % settings.ACCESS_TOKEN,}).json()
        names.extend(data['results'])
        name_url = data['next']
    
    for name in names:
        
        if name['id']==patient_id:
            patients.append(name['first_name'])
            patients.append(name['last_name'])
            patients.append(name['gender'])
   
    return patients

def getcurrentuserinfo():
    response = requests.get('https://drchrono.com/api/users/current', headers={
        'Authorization': 'Bearer %s' % settings.ACCESS_TOKEN,
    });
    response.raise_for_status()
    data = response.json()
    print data
    return data

def authoriseuser(request):
    link = "https://drchrono.com/o/authorize/?redirect_uri="+settings.LOGIN_REDIRECT_URL2+"&response_type=code&client_id="+settings.SOCIAL_AUTH_DRCHRONO_KEY;
    context = {'currentuser': 'Anonymous user','authorizelink':link};
    template_name = "kiosk.html"
    template = get_template(template_name)
    html = template.render(Context(context))
    return HttpResponse(html)


def getuser_token(request):
    template_name = "checkin.html"

    if (settings.ACCESS_TOKEN == None ):
        settings.oauth_code = request.GET.get('code');
        response = requests.post('https://drchrono.com/o/token/', data={
            'code': settings.oauth_code,
            'grant_type': 'authorization_code',
            'redirect_uri': settings.LOGIN_REDIRECT_URL2,
            'client_id': settings.SOCIAL_AUTH_DRCHRONO_KEY,
            'client_secret': settings.SOCIAL_AUTH_DRCHRONO_SECRET,
        })
        data = response.json()
        settings.ACCESS_TOKEN = data['access_token']
        settings.REFRESH_TOKEN = data['refresh_token']
        settings.EXPIRES_IN = data['expires_in']
        refreshtoken.countdown_refresh_accesstoken(settings.EXPIRES_IN)
    data = getcurrentuserinfo()
    username = data['username']
    doc_id = data['doctor']
    appointments = getappointments(doc_id)
    template = get_template(template_name)
    context = {'currentuser': username,"doctors_data":appointments}
    html = template.render(Context(context))
    return HttpResponse(html)
    


