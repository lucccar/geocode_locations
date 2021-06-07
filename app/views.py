from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('basic')


def get_customer_by_id(request):
    return HttpResponse('basic')


def get_all_customers(request):
    return HttpResponse('basic')