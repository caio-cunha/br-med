from django.urls import path
from .views import CotacaoView

urlpatterns = [
    path('cotacao/seed', CotacaoView.seed_dabase, name="seed_dabase"),
]