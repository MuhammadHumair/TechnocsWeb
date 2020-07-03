from django.urls import path
from . import views # . means import views from current directory or we can use app name to import views

urlpatterns = [
    path('', views.index, name='Index')
]
