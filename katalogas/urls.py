from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagrindinis, name='pagrindinis'),
    path('prideti/', views.prideti_knyga, name='prideti_knyga'),
    path('redaguoti/<int:pk>/', views.RedaguotiKnyga.as_view(), name='redaguoti_knyga'),
    path('trinti/<int:pk>/', views.TrintiKnyga.as_view(), name='trinti_knyga'),
    path('statistika/', views.statistika, name='statistika'),
]