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
