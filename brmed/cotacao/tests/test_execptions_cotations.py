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
