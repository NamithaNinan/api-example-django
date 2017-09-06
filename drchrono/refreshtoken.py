import settings
import time
import requests
import threading

def refreshtoken(isRefresh):
    response = "";
    if(isRefresh):
        response = requests.post('https://drchrono.com/o/token/', data={
            'refresh_token': settings.REFRESH_TOKEN,
            'grant_type': 'refresh_token',
            'client_id': settings.SOCIAL_AUTH_DRCHRONO_KEY,
            'client_secret': settings.SOCIAL_AUTH_DRCHRONO_SECRET,
            'redirect_uri' : settings.LOGIN_REDIRECT_URL,
        })
        data = response.json();
        settings.ACCESS_TOKEN = data['access_token'];
        settings.REFRESH_TOKEN = data['refresh_token'];
        settings.EXPIRES_IN = data['expires_in'];
    else:
        response = requests.post('https://drchrono.com/o/revoke_token/', data={
            'client_id': settings.SOCIAL_AUTH_DRCHRONO_KEY,
            'client_secret': settings.SOCIAL_AUTH_DRCHRONO_SECRET,
            'token': settings.ACCESS_TOKEN,
        });
        data = response.json()
        print (data)


def countdown_refresh_accesstoken(t):
    t = threading.Timer(t, refreshtoken(True))
    t.daemon = True
    t.start()
