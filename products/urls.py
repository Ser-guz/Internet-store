from django.urls import path
from . import views

urlpatterns = [
    path('product:<product_id>/', views.ProductView, name='product'),
]
