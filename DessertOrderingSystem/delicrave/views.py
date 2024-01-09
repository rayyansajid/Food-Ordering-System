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
from django.http import JsonResponse
from django.db.models import Count, Sum
from datetime import datetime, timedelta
from django.shortcuts import get_object_or_404



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
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
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
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
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
    
class CustomerCreateView(APIView):
    def get_queryset(self):
        return Customer.objects.all()
    
    def post(self, request, *args, **kwargs):
        name = request.data.get('name')
        username = request.data.get('username')
        password = request.data.get('password')
        User.objects.create_user(username=username,
                                 password=password,
                                 first_name = name)
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
    
class OrdersByCustViewSet(generics.ListAPIView):
    serializer_class = OrderSerializer
    def get_queryset(self):
        custId=self.kwargs["cust_id"]
        return Order.objects.filter(customer=Customer.objects.get(id=custId))
    
class CartItemsByCustViewSet(generics.ListAPIView):
    serializer_class = CartItemSerializer
    def get_queryset(self):
        custId = self.kwargs["cust_id"]
        customer = Customer.objects.get(id = custId)
        print(customer)
        cart = CustomerCart.objects.get(customer = customer)
        print(CartItem.objects.filter(cart=cart))
        return CartItem.objects.filter(cart=cart)
    
class DessertsByCatViewSet(generics.ListAPIView):
    serializer_class = DessertSerializer
    def get_queryset(self):
        dsrtId=self.kwargs["dsrt_id"]
        return Dessert.objects.filter(category = Category.objects.get(id = dsrtId))
    
class OrderHistoryViewset(generics.ListAPIView):
    serializer_class = OrderSerializer
    def get_queryset(self):
        custId = self.kwargs["cust_id"]
        return Order.objects.filter(customer = Customer.objects.get(id = custId)).exclude(status = "Pending") 
                                    # status__exclude = "Pending")
    
class CustomStatsViewSet(APIView):
    def get(request):
        # today's date:
        today = datetime.now().date()
        print(f"today: {today}\n")

        orderitems_today = OrderItem.objects.filter(order__date=today)
        total_items_sold_today = orderitems_today.aggregate(total_items=Sum('quantity'))['total_items'] or 0

        total_orders_today = Order.objects.filter(date=today).count()

        total_desserts = Dessert.objects.count()

        total_categories = Category.objects.count()

        total_flavors = Flavor.objects.count()

        ThisMonthOrderItems = OrderItem.objects.filter(order__date__month=today.month)
        selling_desserts = ThisMonthOrderItems.values('dessert__name').annotate(total_items_sold=Sum('quantity'))
        top_selling_desserts = selling_desserts.order_by('-total_items_sold')[:5]

        start_of_week = today - timedelta(days=today.weekday())

        ThisWeeksOrders = Order.objects.filter(date__gte=start_of_week)
        daily_sales = ThisWeeksOrders.values('date').annotate(total_sale=Sum('totalamount'))

        monthly_sales = Order.objects.values('date__month').annotate(total_sale=Sum('totalamount'))

        response_data = {
            'daysell': total_items_sold_today,
            'dayorders': total_orders_today,
            'totalnoofdesserts': total_desserts,
            'totalcategories': total_categories,
            'totalflavors': total_flavors,
            'topsellingdessert': list(top_selling_desserts),
            'dailysell': list(daily_sales),
            'monthlysale': list(monthly_sales)
        }
        return JsonResponse(response_data)


class DessertsForCustomerView(APIView):
    def get(self, request, custid):
        customer = get_object_or_404(Customer, id=custid)
        desserts_for_customer = Dessert.objects.filter(wishlist__customer=customer)
        serializer = DessertSerializer(desserts_for_customer, many=True)
        return Response(serializer.data)