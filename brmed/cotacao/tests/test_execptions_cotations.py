import json
from unittest.mock import patch
from cotacao.models import Cotacao

from truth.truth import AssertThat


from django.test import (
    TestCase,
    Client
)

class CotacaoTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.client = Client()


    def test_not_found_seed(self):
        """
        GET /apis/cotacao/seed:
        404 Not Found ERROR - Exception Test
        """

        # -------------------------------------------
        # Create the request url WRONG
        request_url = "/ap/cotacao/seed"

        # -------------------------------------------
        # Simulate a http call to the /apis/cotacao/seed endpoint
        response = self.client.get(
            request_url
        )

        # -------------------------------------------
        # Evaluates the status code response
        AssertThat(response.status_code).IsEqualTo(404)

    def test_not_found_chart(self):
        """
        GET /apis/cotacao/chart:
        404 Not Found ERROR - Exception Test
        """

        # -------------------------------------------
        # Create the request url WRONG
        request_url = "/apis/cotacao/chart/"

        # -------------------------------------------
        # Simulate a http call to the /apis/cotacao/chart endpoint
        response = self.client.get(
            request_url
        )

        # -------------------------------------------
        # Evaluates the status code response
        AssertThat(response.status_code).IsEqualTo(404)

    def test_not_found_chart_date(self):
        """
        POST /apis/cotacao/chart/date:
        404 Not Found ERROR - Exception Test
        """

        # -------------------------------------------
        # Create the request url WRONG
        request_url = "/apis/cotacao/chart/date/"

        # -------------------------------------------
        # Simulate a http call to the /apis/cotacao/chart/date endpoint
        response = self.client.post(
            request_url
        )

        # -------------------------------------------
        # Evaluates the status code response
        AssertThat(response.status_code).IsEqualTo(404)

    def test_not_allow_method_chart_date(self):
        """
        POST /apis/cotacao/chart/date:
        404 Not Found ERROR - Exception Test
        """

        # -------------------------------------------
        # Create the request url WRONG
        request_url = "/apis/cotacao/chart/date"

        # -------------------------------------------
        # Simulate a http call to the /apis/cotacao/chart/date endpoint
        response = self.client.get(
            request_url
        )

        # -------------------------------------------
        # Evaluates the status code response
        AssertThat(response.status_code).IsEqualTo(405)
