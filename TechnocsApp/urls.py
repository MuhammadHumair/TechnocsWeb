from django.urls import path
from . import views # . means import views from current directory or we can use app name to import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('clients', views.clients, name='clients'),
    path('team', views.team, name='team'),
    path('faq', views.faqs, name='faq'),
    path('career', views.career, name='career')
]
