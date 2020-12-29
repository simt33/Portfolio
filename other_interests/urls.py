from django.urls import path
from . import views

urlpatterns = [
    path ('', views.OtherInterestsApp, name='other_interests')
]