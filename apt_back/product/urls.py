from django.contrib import admin
from django.urls import path

from .views import ProductListCreateAPIView, ProductRetrieveUpdateAPIView

urlpatterns = [
    path(
        'product/',
        ProductListCreateAPIView.as_view(),
        name='product-list-create',
    ),
    path(
        'product/<int:pk>/',
        ProductRetrieveUpdateAPIView.as_view(),
        name='product-retrieve-update',
    ),
]
