from corsheaders.defaults import default_methods
from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse, JsonResponse
from rest_framework.response import Response
from corsheaders.defaults import default_methods


def index(request):
    return render(request, 'index.html')

def supplier(request):
    return render(request, 'main_app/supplier.html')

def customer(request):
    return render(request, 'main_app/customer.html')

def delivery(request):
    return render(request, 'main_app/delivery.html')
