from django.contrib import admin
from django.urls import path,include
from manage_api import views
from rest_framework import routers


urlpatterns = [
    path('product-list', views.product_list, name='manage_api'),
    path('custom/<int:pk>/', views.product_details, name='custom'),
    path('users', views.UserViewSet.as_view({"get": "list"}), name='users'),
    path('user-details/<int:pk>', views.UserViewSet.as_view({"get": "retrieve"}), name='users'),
]