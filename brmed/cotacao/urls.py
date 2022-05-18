from django.urls import path
from .views import CotacaoView

urlpatterns = [
    path('cotacao', CotacaoView.as_view(), name="cotacao"),
]