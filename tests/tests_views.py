from django.http import response
from django.test import TestCase, Client
from django.urls import reverse
from app.views import CustomerView
from core.models import Customer


class TestViews(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.all_customers = reverse('all-customers')
        self.customer = Customer.objects.create(
            id=1,
            first_name="Lucas",
            last_name="Carvalho",
            email="lucas.crvlh.s@gmail.com",
            gender="Male",
            company="Oowlish",
            city="Rio",
            title="Developer",
            latitude=77.2254,
            longitude=-43.20114,
        )
        self.customer_by_id = reverse('customer-by-id', args=[1])


    def test_customer_all(self):
        response = self.client.get(self.all_customers)
        self.assertEquals(response.status_code, 200)


    def test_customer_by_id(self):

        response = self.client.get(self.customer_by_id)
        print(response.json())
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.json()[0]["fields"]["latitude"], 77.2254)
