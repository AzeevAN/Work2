from django.contrib.auth.models import AbstractUser
from django.db import models


class Store(AbstractUser):
    inn = models.TextField(null=True, blank=True) # номер телефона пользователя
    year_open = models.PositiveIntegerField(null=True, blank=True) # возраст пользователя
    # salary_amount = models.FloatField(null=True, blank=True) # зарплата пользователя
