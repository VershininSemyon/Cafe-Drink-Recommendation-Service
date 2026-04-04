
import logging

from django.conf import settings
from django.core.cache import cache
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import SessionAuthentication
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from .filters import DrinkFilter
from .models import Drink
from .serializers import DrinkSerializer


class DrinkViewSet(ReadOnlyModelViewSet):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer

    permission_classes = [AllowAny]
    authentication_classes = [JWTAuthentication, SessionAuthentication]

    filterset_class = DrinkFilter
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    ]

    search_fields = ['name', 'description']
    ordering_fields = ['strength', 'sweetness', 'bitterness']

    def get_queryset(self):
        cache_key = settings.CACHE_KEYS['DRINKS_LIST']['KEY']
        cache_ttl = settings.CACHE_KEYS['DRINKS_LIST']['TTL']

        if not cache.get(cache_key):
            value = super().get_queryset()
            cache.set(cache_key, value, cache_ttl)
        
        return cache.get(cache_key)
