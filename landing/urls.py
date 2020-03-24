from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.HomeView, name='home'),
    url(r'^landing_page/$', views.LandingView, name='landing_page'),
]
