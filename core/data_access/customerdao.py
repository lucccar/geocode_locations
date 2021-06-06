from core.models import Customer

class CustomerDAO:

    def get_all_customers(self) -> list:

        print("Getting all customers the database...")
        return Customer.objects.all()


    def get_customer_by_id(self, id: int) -> list:

        print("Getting customer {} the database...".format(id))
        return Customer.objects.get(pk=id)


    def initialize_customer_table(self, customer) -> None:

        print("Inserting customer into the database...")
        customer.save()
        
