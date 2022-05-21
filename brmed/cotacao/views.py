from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from cotacao.serializers import CotacaoSerializer 
from cotacao.services import CotacaoService
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import TemplateHTMLRenderer
from cotacao.forms import DateForm

class CotacaoView(APIView):

    @api_view(['GET'])
    def seed_dabase(self):
        """
            A View for get data in VAT endpoint and put in database local
        """
        cotacao_service = CotacaoService()
        message = cotacao_service.seed()
        return Response(message)

    @api_view(['GET'])
    @renderer_classes([TemplateHTMLRenderer])
    def initial_chart(self):
        """
            A View for get and send data
        """
        cotacao_service = CotacaoService()
        datas_final = cotacao_service.get_data_initial_chart()
        context = {
            'dates': datas_final['dates'],
            'real': datas_final['real'],
            'euro': datas_final['euro'],
            'iene': datas_final['iene'],
            'errors': datas_final['errors']
        }
        return Response(context, template_name='index.html')

    @api_view(['POST'])
    @renderer_classes([TemplateHTMLRenderer])
    def date_chart(request):
        """
            A View for get and send data
        """
        if request.method == "POST":
            form = DateForm(request.POST)
            if form.is_valid():
                date_initial = form.cleaned_data['date_initial']
                date_final = form.cleaned_data['date_final']
                cotacao_service = CotacaoService()
                datas_final = cotacao_service.get_data_date_chart(date_initial, date_final)
                context = {
                    'dates': datas_final['dates'],
                    'real': datas_final['real'],
                    'euro': datas_final['euro'],
                    'iene': datas_final['iene'],
                    'errors': datas_final['errors']
                }
                return render(request, 'index.html', context)
            else:
                context = {'dates': [], 'real': [], 'euro': [], 'iene': [], 'errors': "Selecione as Datas!"}
                return render(request, 'index.html', context)
    
    @api_view(['GET'])
    def get_all_cotations(self):
        """
            A View for get all cotations saved in database
        """
        cotacao_service = CotacaoService()
        data = cotacao_service.get_all()     
        cotacao_serializer = CotacaoSerializer(data, many=True)   
        return Response(cotacao_serializer.data)            
