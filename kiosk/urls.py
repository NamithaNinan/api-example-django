from django.conf.urls import url
import views


urlpatterns = [
    #url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),

    #url(r'', include('social.apps.django_app.urls', namespace='social')),

   url(r'^$', views.authorize),
    url(r'^login/$', views.gets_token),

]
