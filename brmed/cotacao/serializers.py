from rest_framework import serializers
from cotacao.models import Cotacao

class CotacaoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cotacao
        fields = ('id', 'real', 'euro', 'iene')
