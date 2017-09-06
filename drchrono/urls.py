from django.conf.urls import include, url, patterns
from django.views.generic import TemplateView
from django.contrib import admin
import views
import settings

urlpatterns = [
    #url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),

    #url(r'', include('social.apps.django_app.urls', namespace='social')),

   url(r'^$', views.authorisedoc),
    url(r'^login/$' , views.get_token),
    #url(r'^kiosk/', include('kiosk.urls')),
    url(r'^kiosk/$', views.authoriseuser),
    url(r'^kiosk/login/$', views.getuser_token),
    url(r'^admin/',include(admin.site.urls)),

]
