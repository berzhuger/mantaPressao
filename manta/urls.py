from . import views
from django.conf.urls import url
from manta import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers


router = routers.SimpleRouter()
urlpatterns = [
    #url(r'^', views.HomePageView.as_view(), name='home'),

]