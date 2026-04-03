
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from .views import CustomTokenObtainPairView


urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='token-auth'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token-verify'),
]
