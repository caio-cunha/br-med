from django.db import models
from model_utils.models import TimeStampedModel
from datetime import datetime

class Cotacao(TimeStampedModel):

    real = models.DecimalField(max_digits=30, decimal_places=25)
    euro = models.DecimalField(max_digits=30, decimal_places=25)
    iene = models.DecimalField(max_digits=30, decimal_places=25)
    date = models.DateField(default=datetime.now, null=False, unique=True,error_messages={'unique':"Cotações já importadas!"})
