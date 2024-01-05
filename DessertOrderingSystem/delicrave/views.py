# from django.shortcuts import render
# import io
# from rest_framework.parsers import JSONParser
# from .serializers import *
# from rest_framework.renderers import JSONRenderer
# from django.http import HttpResponse
# from rest_framework.response import Response
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.decorators import action
# from rest_framework import viewsets
# from .models import *

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
        
# class CustomerViewSet(viewsets.ModelViewSet):
#     queryset = Customer.objects.all()
#     serializer_class = CustomerSerializer

#     def create(self, request, *args, **kwargs):
#         user = User.objects
#         return super().create(request, *args, **kwargs)

    # @action(detail=True, methods=['get'])
    # def customer(self, request, pk = 0):
    #     print("I am in customer")
    #     # customer = Customer.objects.get(pk = pk)
    #     customer = self.get_object()
    #     print(customer)
    #     cust_serializer = CustomerSerializer(data=customer,
    #                                          context = {'request':request})
    #     print(cust_serializer)
    #     return Response(cust_serializer.data)
    
# class DessertViewSet(viewsets.ModelViewSet):
#     queryset = Dessert.objects.all()
#     serializer_class = DessertSerializer

    # @action(detail=True, methods=['get'])
    # def dessert(self, request, pk = 0):
    #     dessert = Dessert.objects.get(pk = pk)
    #     dsrt_serializer = DessertSerializer(dessert,
    #                                         context = {'request':request})
    #     return Response(dsrt_serializer.data)


from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authtoken.models import Token
from .models import *
from .serializers import *
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from rest_framework.views import APIView


class CustomerViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class FlavorViewSet(viewsets.ModelViewSet):
    queryset = Flavor.objects.all()
    serializer_class = FlavorSerializer


class DessertViewSet(viewsets.ModelViewSet):
    queryset = Dessert.objects.all()
    serializer_class = DessertSerializer

class OrderViewSet(viewsets.ModelViewSet):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class FlavorCatViewSet(viewsets.ModelViewSet):
    queryset = FlavorCat.objects.all()
    serializer_class = FlavorCatSerializer


class WishlistViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer


class CustomerCartViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = CustomerCart.objects.all()
    serializer_class = CustomerCartSerializer


class CartItemViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer


class OrderItemViewSet(viewsets.ModelViewSet):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class LoginView(generics.GenericAPIView):
    serializer_class = CustomerSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        print(username)
        password = request.data.get('password')
        print(password)
        user = authenticate(username=username, password = password)
        print(user)
        if user is None:
            return Response({'error': 'Invalid Credentials'}, status=401)

        token, created = Token.objects.get_or_create(user=user)
        print(created)
        return Response({'token': token.key})
    
# class MultipleModelObjCreateView(viewsets.ViewSet):
#     def get_queryset(self, model):
#         queryset = {
#             "Customer" : Customer.objects.all(),
#             "FlavorCat" : FlavorCat.objects.all(),
#             "Flavor" : Flavor.objects.all(),
#             "Category" : Category.objects.all()
#         }
#         return queryset[model]
    

#     def customer(self, request, *args, **kwargs):
#         print(request)
#         return Response({'msg':"check 1 2 3"})
    
class CustomerCreateView(APIView):
    def get_queryset(self):
        return Customer.objects.all()
    
    def post(self, request, *args, **kwargs):
        name = request.data.get('name')
        contact = request.data.get('contact')
        email = request.data.get('email')
        address = request.data.get('address')
        username = request.data.get('username')
        password = request.data.get('password')
        User.objects.create_user(username=username, password=password, first_name = name)
        print(Customer.objects.create(request.data))
        return Response({'msg':'Customer Created'})
    

class LogoutView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        return Response({'message': 'Logout successful'})
    

class ItemsByOrderViewSet(generics.ListAPIView):
    serializer_class = OrderItemSerializer
    def get_queryset(self):
        OrderId=self.kwargs["order_id"]
        return OrderItem.objects.filter(order=Order.objects.get(id=OrderId))