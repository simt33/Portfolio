from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.tech_page, name='tech')
]