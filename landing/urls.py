from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home_view, name='home'),
    url(r'^landing_page/$', views.landing_view, name='landing_page'),
]
