from sqlite3 import Date
from rest_framework.views import APIView
from rest_framework.response import Response 
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
        message = cotacao_service.seed_initial()
        return Response(message)

    @api_view(['GET'])
    @renderer_classes([TemplateHTMLRenderer])
    def initial_chart(self):
        cotacao_service = CotacaoService()
        dates, data_real, data_euro, data_iene = cotacao_service.get_data_initial_chart()
        context = {'dates': dates, 'real': data_real, 'euro': data_euro, 'iene': data_iene}
        return Response(context, template_name='index.html')

    @api_view(['POST'])
    @renderer_classes([TemplateHTMLRenderer])
    def date_chart(request):
        if request.method == "POST":
            form = DateForm(request.POST)
            if form.is_valid():
                date_initial = form.cleaned_data['date_initial']
                date_final = form.cleaned_data['date_final']
                cotacao_service = CotacaoService()
                dates, data_real, data_euro, data_iene = cotacao_service.get_data_date_chart(date_initial, date_final)
                context = {'dates': dates, 'real': data_real, 'euro': data_euro, 'iene': data_iene}
        return Response(context,template_name='index.html')
