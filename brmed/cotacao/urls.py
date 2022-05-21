from django.urls import path
from .views import CotacaoView

urlpatterns = [
    path('cotacao/seed', CotacaoView.seed_dabase, name="seed_dabase"),
    path('cotacao/chart', CotacaoView.initial_chart, name="initial_chart"),
    path('cotacao/chart/date', CotacaoView.date_chart, name="date_chart"),
    path('cotacao/getall', CotacaoView.get_all_cotations, name="get_all")

]