from django.db import models
from model_utils.models import TimeStampedModel
from datetime import datetime

class Cotacao(TimeStampedModel):

    real = models.FloatField(null=True, blank=True)
    euro = models.FloatField(null=True, blank=True)
    iene = models.FloatField(null=True, blank=True)
    date = models.DateField(default=datetime.now, null=False, unique=True, error_messages={'unique':"Cotações já importadas!"})
