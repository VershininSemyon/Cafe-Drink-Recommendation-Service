
from django.urls import path
from . import views


urlpatterns = [
    path('register/initiate/', views.initiate_registration, name='initiate-registration'),
    path('register/complete/<uuid:token>/', views.complete_registration, name='complete-registration'),
    path('register/resend/', views.resend_registration_email, name='resend-registration'),
]
