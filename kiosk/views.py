import requests
from drchrono import settings
import refreshtoken
from datetime import datetime
from django.template import Context
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.template.loader import get_template
from django.views.generic.base import TemplateView

def authorize(request):
    link = "https://drchrono.com/o/authorize/?redirect_uri="+settings.LOGIN_REDIRECT_URL2+"&response_type=code&client_id="+settings.SOCIAL_AUTH_DRCHRONO_KEY;
    context = {'currentuser': 'Anonymous user','authorizelink':link};
    template_name = "index.html"
    template = get_template(template_name)
    html = template.render(Context(context))
    print "bye"
    return HttpResponse(html)


def getuser_token(request):
    template_name = "checkin.html"
    print "hello!"
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
    
    template = get_template(template_name)
    context = {'currentuser': username}
    html = template.render(Context(context))
    return HttpResponse(html)

def getcurrentuserinfo():
    response = requests.get('https://drchrono.com/api/users/current', headers={
        'Authorization': 'Bearer %s' % settings.ACCESS_TOKEN,
    });
    response.raise_for_status()
    data = response.json()
    print data
    return data
