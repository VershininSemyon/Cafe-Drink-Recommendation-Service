
from django_filters import rest_framework

from .models import Drink


class DrinkFilter(rest_framework.FilterSet):
    class Meta:
        model = Drink
        fields = {
            'strength': ['exact'],
            'sweetness': ['exact'],
            'bitterness': ['exact'],
            'temperature': ['exact'],
            'caffeine_free': ['exact'],
            'milk_based': ['exact'],
        }
