from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response 
from cotacao.services import CotacaoService

class CotacaoView(APIView):

    def get(self, request):
        """
            A View for get data in VT and put in database local
            Args: \n
                request: Http request
            
            Returns: \n
            
        """
        cotacao_service = CotacaoService()
        cotacoes = cotacao_service.seed_initial()
        return Response(cotacoes)