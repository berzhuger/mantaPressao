from . import views
from django.conf.urls import url
from manta import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers



router = routers.SimpleRouter()
urlpatterns = [
    #url(r'^', views.HomePageView.as_view(), name='home'),
    url(r'^paciente/$',  views.PacienteList.as_view()),    
    url(r'^paciente/(?P<pk>[0-9]+)/$', views.PacienteDetail.as_view()), 
    url(r'^avaliacao/$',  views.AvaliacaoList.as_view()),    
    url(r'^avaliacao/(?P<pk>[0-9]+)/$', views.AvaliacaoDetail.as_view()), 
    url(r'^dadosSensor/$',  views.SensorList.as_view()),    
    url(r'^dadosSensor/(?P<pk>[0-9]+)/$', views.SensorDetail.as_view()), 
]