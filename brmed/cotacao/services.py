"""

Author: Caio Henrique Oliveira Cunha

Here it is concentrated as business rules

"""
import coreapi
import datetime 
from cotacao.models import Cotacao
from cotacao.serializers import CotacaoSerializer
from requests.exceptions import ConnectionError
from brmed.settings import BASE_URL_ENDPOINT_VAT, BASE_COTATION

class CotacaoService():

    def _get_save_data_api(self, date):
        """
        A service to seed database with 5 response of VAT ENDPOINT 

            Args:   \n
                date : Date for search in VAT API

            Returns:  \n  
                data_dict: data of getted in VAT API or message error
        """

        client = coreapi.Client()

        date_str = date.strftime("%Y-%m-%d")
        filter = Cotacao.objects.filter(date=date_str)

        if not filter:
            
            try:

                data = client.get(BASE_URL_ENDPOINT_VAT + '?base=' + BASE_COTATION + '&date=' + date_str)

            except ConnectionError as e:

                raise e
            
            data_dict = {}

            try:

                data_dict["real"] = data["rates"]["BRL"]
                data_dict["euro"] = data["rates"]["EUR"]
                data_dict["iene"] = data["rates"]["JPY"]
                data_dict["date"] = data["date"]
                data_dict["message"] = "Dados Importados!"

            except KeyError as exp:

                raise exp

            cotacao_serializer = CotacaoSerializer(data=data_dict)
            if (cotacao_serializer.is_valid()):
                cotacao_serializer.save()
            
            return data_dict

        else:
            
            data_dict = {'date': '', 'message': "Dados não importados! O registro já está salvo."}

        return data_dict

    
    def seed(self):
        """
        A service seed database with 5 response of VAT ENDPOINT 

            Args:   \n
                - : None

            Returns:  \n  
                message: sucess message or error
        """
        message = []
        limit = 0
        day_cont = 0
        date_initial = datetime.datetime.today()

        while (limit <= 4):

            date = date_initial - datetime.timedelta(days=day_cont)

            weekday = date.weekday()

            if weekday < 5:
                
                data = self._get_save_data_api(date)
            
                if data["date"] != '':

                    limit = limit + 1

                date_str = date.strftime("%Y-%m-%d")
                message.append(date_str + ': ' + data["message"])

            day_cont = day_cont + 1

        return message  
        

    def get_data_initial_chart(self):
        """
        A service to get and organize data from database, getting the last 5 cotations in relation USD

            Args:   \n
                - : None

            Returns:  \n  
                datas_final : data of cotations from database or errors 

        """
        datas_final = {'dates': [], 'real': [], 'euro': [], 'iene': [], 'errors': ''}

        date_inicial = datetime.datetime.today() - datetime.timedelta(days=6)
        date_inicial_str = date_inicial.strftime("%Y-%m-%d")

        date_final = datetime.datetime.today()
        date_final_str = date_final.strftime("%Y-%m-%d")

        if date_inicial.weekday == 5:
            date_inicial = date_inicial - datetime.timedelta(days=1)
        elif date_inicial.weekday == 6:
            date_inicial = date_inicial - datetime.timedelta(days=2)

        ## get records with date range selected
        datas = Cotacao.objects.filter(date__range=[date_inicial_str, date_final_str]).order_by('date')

        if not datas:
            datas_final['errors'] = "Nenhum dado encontrado no BANCO DE DADOS!"
            return datas_final
        
        for data in datas:

            date_str = data.date.strftime("%Y-%m-%d")
            datas_final['dates'].append(date_str)
            datas_final['real'].append(data.real)
            datas_final['euro'].append(data.euro)
            datas_final['iene'].append(data.iene)

        return datas_final 

    def get_data_date_chart(self, date_inicial, date_final):
        """
        A service to get and organize data from database, using date selected by user

            Args:   \n
                date_inicial : Date Initial for generate chart
                date_final: Date Final for generate chart

            Returns:  \n  
                datas_final : data of cotations or errors
        """
        
        datas_final = {'dates': [], 'real': [], 'euro': [], 'iene': [], 'errors': ''}

        diferenca = date_final - date_inicial
        if diferenca.days > 5:
            datas_final['errors'] = "Selecione um intervalo de no máximo 5 dias!"
            return datas_final

        if date_inicial > date_final:
            datas_final['errors'] = "Selecione uma Data Inicial menor que a Data Final!"
            return datas_final

        for i in range(0,5):

            date = date_final - datetime.timedelta(days=i)
            data = self._get_save_data_api(date)

        ## get records with date range selected
        datas = Cotacao.objects.filter(date__range=[date_inicial, date_final]).order_by('-id')

        if not datas:
            datas_final['errors'] = "Não há dados para a data selecionada!"
            return datas_final
        
        for data in datas:

            date_str = data.date.strftime("%Y-%m-%d")
            datas_final['dates'].append(date_str)
            datas_final['real'].append(data.real)
            datas_final['euro'].append(data.euro)
            datas_final['iene'].append(data.iene)

        return datas_final

    def get_all(self):
        """
        A service to get all cotation saved in database

            Args:   \n
                - : None

            Returns:  \n  
                cotacao : data of all cotations
        """

        ## Note: As the amount of data available in the database will be small, this query would not be costly..
        ## Note02: In a scenario where the quote table grows a lot, some strategy is needed to make this query
        ## Note03: Pagination for example, limiting the amount of searches in the bank.
        cotacao = Cotacao.objects.all()
        
        return cotacao

