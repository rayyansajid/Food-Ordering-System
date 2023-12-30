from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .serializers import CustomerSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def createCustomer(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream=stream)
        serializer = CustomerSerializer(data = pythondata)
        if serializer.is_valid():
            serializer.save()
            msg = {
                'msg':'Successfully created Customer Object'
            }
            json_data = JSONRenderer().render(data = msg)
            return HttpResponse(json_data, content_type = 'application/json')
        json_data = JSONRenderer().render(data = serializer.errors)
        return HttpResponse(json_data, content_type = 'application/json')
        