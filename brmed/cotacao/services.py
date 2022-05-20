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

    def seed_initial(self):
        """
        A service seed database with 5 latest response of VAT ENDPOINT 

            Args:   \n
                - : None

            Returns:  \n  
                message: sucess message or error
        """
         
        client = coreapi.Client()
        date_validation = []
        limit = 0
        day_cont = 0
        message = "Importação realizada!"

        while (limit <= 4):

            date = datetime.datetime.today() - datetime.timedelta(days=day_cont)
            date_str = date.strftime("%Y-%m-%d")
            data_dict = {}

            try:
                data = client.get(BASE_URL_ENDPOINT_VAT + '?base=' + BASE_COTATION + '&date=' + date_str)
            except ConnectionError as e:
                raise e

            try:
                data_dict["real"] = data["rates"]["BRL"]
                data_dict["euro"] = data["rates"]["EUR"]
                data_dict["iene"] = data["rates"]["JPY"]
                data_dict["date"] = data["date"]
            except KeyError as exp:
                raise exp
            
            if data_dict["date"] not in date_validation:

                cotacao_serializer = CotacaoSerializer(data=data_dict)
                cotacao_serializer.is_valid(raise_exception=True)
                cotacao_serializer.save()
                
                date_validation.append(data_dict["date"])
                limit = limit + 1
            
            day_cont = day_cont + 1
            
        return message

    def get_data_initial_chart(self):
        """
        A service to get and organize data from database, getting the last 5 cotations in relation USD

            Args:   \n
                - : None

            Returns:  \n  
                dates : dates of plot
                real: real cotation \n 
                euro: euro cotation \n 
                iene: iene cotation \n 

        """
        datas_final = {'dates': [], 'real': [], 'euro': [], 'iene': [], 'errors': ''}

        date_inicial = datetime.datetime.today() - datetime.timedelta(days=4)
        date_inicial_str = date_inicial.strftime("%Y-%m-%d")

        date_final = datetime.datetime.today()
        date_final_str = date_final.strftime("%Y-%m-%d")

        ## get records with date range selected
        datas = Cotacao.objects.filter(date__range=[date_inicial_str, date_final_str])

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
                datas_final : data of cotations and errors
        """
        
        datas_final = {'dates': [], 'real': [], 'euro': [], 'iene': [], 'errors': ''}

        diferenca = date_final - date_inicial
        if diferenca.days > 5:
            datas_final['errors'] = "Selecione um intervalo de no máximo 5 dias!"
            return datas_final

        if date_inicial > date_final:
            datas_final['errors'] = "Selecione uma Data Inicial menor que a Data Final!"
            return datas_final

        ## get records with date range selected
        datas = Cotacao.objects.filter(date__range=[date_inicial, date_final])
        
        for data in datas:

            date_str = data.date.strftime("%Y-%m-%d")
            datas_final['dates'].append(date_str)
            datas_final['real'].append(data.real)
            datas_final['euro'].append(data.euro)
            datas_final['iene'].append(data.iene)

        return datas_final

