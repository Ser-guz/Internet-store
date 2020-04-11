from django.conf.urls import url
from .views import basket_adding, checkout

urlpatterns = [
    url(r'^basket_adding/$', basket_adding, name='basket_adding'),
    url(r'^checkout/$', checkout, name='checkout'),
]
