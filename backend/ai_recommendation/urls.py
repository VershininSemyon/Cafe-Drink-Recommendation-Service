
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import dialog, message, answer


urlpatterns = [
    path('dialogs/', dialog.ListCreateDialogAPIView.as_view()),
    path('dialogs/<str:pk>/', dialog.RetrieveDestroyDialogAPIView.as_view()),
]
