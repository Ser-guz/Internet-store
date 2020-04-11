from django.urls import path
from .views import ProductDetail

urlpatterns = [
    path('product:<pk>/', ProductDetail.as_view(), name='product'),
]
