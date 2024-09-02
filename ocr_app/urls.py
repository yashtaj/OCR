from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('result/<int:pk>/', views.result, name='result'),  # Added path for result view
    path('download_txt/', views.download_txt, name='download_txt'),
    path('download_pdf/', views.download_pdf, name='download_pdf'),
]
