from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .serializers import *
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
# from django.views.decorators import action
from rest_framework import viewsets
from .models import *

# # Create your views here.
# @csrf_exempt
# def createCustomer(request):
#     if request.method == 'POST':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream=stream)
#         serializer = CustomerSerializer(data = pythondata)
#         if serializer.is_valid():
#             serializer.save()
#             msg = {
#                 'msg':'Successfully created Customer Object'
#             }
#             json_data = JSONRenderer().render(data = msg)
#             return HttpResponse(json_data, content_type = 'application/json')
#         json_data = JSONRenderer().render(data = serializer.errors)
#         return HttpResponse(json_data, content_type = 'application/json')
        
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    # @action(detail=True, methods=['get'])
    def customer(self, request, pk = 0):
        customer = Customer.objects.get(pk = pk)
        cust_serializer = CustomerSerializer(customer,
                                             context = {'request':request})
        return Response(cust_serializer.data)
    
class DessertViewSet(viewsets.ModelViewSet):
    queryset = Dessert.objects.all()
    serializer_class = DessertSerializer

    # @action(detail=True, methods=['get'])
    def dessert(self, request, pk = 0):
        dessert = Dessert.objects.get(pk = pk)
        dsrt_serializer = DessertSerializer(dessert,
                                            context = {'request':request})
        return Response(dsrt_serializer.data)
    
