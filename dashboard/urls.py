from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='dashboard-home'),
    path('api-docs/', views.api_docs, name='api-docs'),
]