from django.urls import path
from . import views

urlpatterns = [path("", views.formularz, name="formularz")]
