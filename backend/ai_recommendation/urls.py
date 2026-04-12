
from django.urls import path

from .views import dialog, message


urlpatterns = [
    path('dialogs/', dialog.ListCreateDialogAPIView.as_view()),
    path('dialogs/<str:pk>/', dialog.RetrieveDestroyDialogAPIView.as_view()),

    path('messages/', message.ListCreateMessageAPIView.as_view()),
    path('messages/<str:pk>/', message.RetrieveDestroyMessageAPIView.as_view()),
]
