from django.db import models
from model_utils.models import TimeStampedModel


class Cotacao(TimeStampedModel):

    real = models.DecimalField(max_digits=20, decimal_places=10)
    euro = models.DecimalField(max_digits=20, decimal_places=10)
    iene = models.DecimalField(max_digits=20, decimal_places=10)
