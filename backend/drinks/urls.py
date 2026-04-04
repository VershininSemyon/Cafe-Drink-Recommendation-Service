
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import DrinkViewSet


router = DefaultRouter()
router.register(r'', DrinkViewSet)


urlpatterns = [
    path('', include(router.urls))
]
