
from django.db import models


class Drink(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    strength = models.PositiveSmallIntegerField(
        choices=[(1, "Очень слабая"), (2, "Слабая"), (3, "Средняя"), (4, "Крепкая"), (5, "Очень крепкая")]
    )
    sweetness = models.PositiveSmallIntegerField(
        choices=[(1, "Без сахара"), (2, "Слабая сладость"), (3, "Средняя"), (4, "Сладкий"), (5, "Очень сладкий")]
    )
    bitterness = models.PositiveSmallIntegerField(
        choices=[(1, "Нет горечи"), (2, "Слабая"), (3, "Средняя"), (4, "Выраженная"), (5, "Очень горький")]
    )
    
    temperature = models.CharField(
        max_length=10,
        choices=[("hot", "Горячий"), ("cold", "Холодный"), ("any", "Любой")]
    )

    caffeine_free = models.BooleanField(default=False)
    milk_based = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
