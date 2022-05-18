from django.db import models
from model_utils.models import TimeStampedModel
from datetime import datetime

class Cotacao(TimeStampedModel):

    real = models.DecimalField(max_digits=20, decimal_places=15)
    euro = models.DecimalField(max_digits=20, decimal_places=15)
    iene = models.DecimalField(max_digits=20, decimal_places=15)
    date = models.DateField(default=datetime.now)
