from django.conf.urls import url
from .views import HomeListView, LandingCreateView

urlpatterns = [
    url(r'^$', HomeListView.as_view(), name='home'),
    # url(r'^landing_page/$', landing_view, name='landing_page'),
    url(r'^landing_page/$', LandingCreateView.as_view(), name='landing_page'),
]
