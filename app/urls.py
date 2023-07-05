# Use include() to add paths from the catalog application
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Inicio.as_view(), name='inicio'),
]