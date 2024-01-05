from django.contrib import admin
from django.urls import path, include
from delicrave import views
from rest_framework.routers import DefaultRouter
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'flavors', FlavorViewSet)
router.register(r'desserts', DessertViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'flavorcats', FlavorCatViewSet)
router.register(r'wishlists', WishlistViewSet)
router.register(r'customercarts', CustomerCartViewSet)
router.register(r'cartitems', CartItemViewSet)
router.register(r'orderitems', OrderItemViewSet)
# router.register(r'custcreate', CustomerCreateView)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # path('customer/<int:pk>/', CustomerViewSet.as_view({'get':'retrieve'}))
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('createcustomer/', CustomerCreateView.as_view(), name="Create Customer"),
    path('itemsbyOrder/<int:order_id>/',ItemsByOrderViewSet.as_view(), name="ItemsByOrder"),
]

# from django.urls import path
# from rest_framework.authtoken.views import obtain_auth_token
# from rest_framework import permissions
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# urlpatterns = [
#     # Obtain JWT token
#     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

#     # Refresh JWT token
#     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

#     # Obtain auth token (for TokenAuthentication)
#     path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

#     # Add your other API endpoints
#     # ...
# ]
