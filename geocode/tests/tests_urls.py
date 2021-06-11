from django.test import SimpleTestCase
from django.urls import resolve, reverse
from app.views import CustomerView

class TestsUrls(SimpleTestCase):
    
    def test_all_customers(self):
        url = reverse("all-customers")
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, CustomerView)

    def test_customer_by_id(self):
        for arg in [24, 666, 42]:
            url = reverse("customer-by-id", args=[arg])
            print(resolve(url))
            self.assertEquals(resolve(url).func.view_class, CustomerView)