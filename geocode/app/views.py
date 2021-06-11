from django.http import HttpResponse
from core.data_access.customerdao import CustomerDAO
from rest_framework.views import APIView

class CustomerView(APIView):


    def get(self, request, id=None):
        if request.method == 'GET':
            if id == None:
                return HttpResponse(CustomerDAO.get_all_customers(), content_type="application/json")
            else:
                return HttpResponse(CustomerDAO.get_customer_by_id(id=id), content_type="application/json")
        else: HttpResponse('Method not allowed')
