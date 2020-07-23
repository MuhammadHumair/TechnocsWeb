from django.urls import path
from adminpanel import views
from account import views as acc_view

urlpatterns = [
    path('', views.index, name='index'),

    path('faqs', views.faqs, name='faqs'),
    path('editFaq/<int:id>/', views.editFaq, name='editFaq'),
    path('faqStatus/<str:status>/<int:id>/', views.faqStatus, name='faqStatus'),
    
    path('inquiry', views.inquiry, name='inquiry'),
    path('inquiryStatus/<str:status>/<int:id>/', views.inquiryStatus, name='inquiryStatus'),

    path('categoryTags', views.categoryTags, name='categoryTags'),
    path('category', views.category, name='category'),
    path('tagStatus/<str:status>/<int:id>/', views.tagStatus, name='tagStatus'),
    path('tagCategoryStatus/<str:status>/<int:id>/', views.tagCategoryStatus, name='tagCategoryStatus'),

    path('services', views.services, name='services'),
    path('projects', views.projects, name='projects'),

    path('clients', views.clients, name='clients'),
    path('clientStatus/<str:status>/<int:id>/', views.clientStatus, name='clientStatus'),

    path('team', views.team, name='team'),
    path('teamStatus/<str:status>/<int:id>/', views.teamStatus, name='teamStatus'),

    path('account/logout', acc_view.logout, name='logout')
]
