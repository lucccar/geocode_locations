from django.core import serializers
from core.models import Customer

class CustomerDAO:

    @staticmethod
    def get_all_customers() -> list:

        print("Getting all customers the database...")
        return serializers.serialize('json', Customer.objects.all())


    @staticmethod
    def get_customer_by_id(id: int) -> list:

        print("Getting customer {} the database...".format(id))
        data = Customer.objects.get(pk=id)
        return serializers.serialize('json', [data], ensure_ascii=False)


    def initialize_customer_table(self, customer) -> None:

        print("Inserting customer into the database...")
        customer.save()
        
