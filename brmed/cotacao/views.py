from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response 
from cotacao.services import CotacaoService
from rest_framework.decorators import api_view

class CotacaoView(APIView):

    @api_view(['GET'])
    def seed_dabase(self):
        """
            A View for get data in VAT endpoint and put in database local
        """
        cotacao_service = CotacaoService()
        message = cotacao_service.seed_initial()
        return Response(message)