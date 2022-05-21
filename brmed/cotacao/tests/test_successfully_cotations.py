import json
from unittest.mock import patch
from cotacao.models import Cotacao
from cotacao.forms import DateForm

from truth.truth import AssertThat

from django.test import (
    TestCase,
    Client
)

class CotacaoTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.client = Client()

        # -------------------------------------------
        # Create a cotacao on the DB
        cls.cotacao = Cotacao.objects.create(
            real=3.58,
            euro=5.50,
            iene=4.89,
            date='2022-05-21'
        )
    
    def test_successfully_seed_database(self):
        """
        GET /apis/cotacao/seed
        successfully seed database with 5 register
        """

        # -------------------------------------------
        # Create the request url
        request_url = "/apis/cotacao/seed"

        # -------------------------------------------
        # Simulate a http call to the /apis/cotacao/seed endpoint
        response = self.client.get(
            request_url,
        )

        # -------------------------------------------
        # Evaluates the status code response
        AssertThat(response.status_code).IsEqualTo(200)

        # -------------------------------------------
        # Evaluates if the 5 records getted in VAT API was save in database
        contacao = Cotacao.objects.all()
        # Is 6 because one was registred above (setUp)
        AssertThat(len(contacao)).IsEqualTo(6)
        

    def test_successfully_chart_initial(self):
        """
        GET /apis/cotacao/chart
        successfully get data in database and to plot
        """

        # -------------------------------------------
        # Create the request url
        request_url = "/apis/cotacao/chart"

        # -------------------------------------------
        # Simulate a http call to the /apis/cotacao/chart endpoint
        response = self.client.get(
            request_url,
        )

        # -------------------------------------------
        # Evaluates the status code response
        AssertThat(response.status_code).IsEqualTo(200)

        # -------------------------------------------
        # Evaluates if cotation sabe in SetUp was returned by this endpoint
        cotacao = Cotacao.objects.filter(date=self.cotacao.date).first()
        date_str = cotacao.date.strftime("%Y-%m-%d")]
        AssertThat(date_str).IsEqualTo(response.context['dates'][0])

        # -------------------------------------------
        # Check if Template is Used
        self.assertTemplateUsed(response, 'index.html')

        # -------------------------------------------
        # Check if HTML has some tags
        self.assertContains(response, '<form')
        self.assertContains(response, 'type="date"',2)

        # -------------------------------------------
        # Check if CSRF token is set in HTML
        self.assertContains(response, 'csrfmiddlewaretoken')

       


        