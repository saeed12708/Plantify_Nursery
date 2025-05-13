from django.shortcuts import render
from .serializers import SignupSerializer, UserSerializer, LoginSerializer
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import User
from rest_framework import viewsets, permissions
from .models import UserProfile,HomeBanner

from .serializers import UserProfileSerializer
from .models import Order
from .serializers import OrderSerializer
from .models import Cart, Favorite, Notification,Blog, Location, Offer
from .serializers import CartSerializer, FavoriteSerializer, NotificationSerializer
from .serializers import BlogSerializer, LocationSerializer, OfferSerializer
from .models import PaymentMethod
from .serializers import PaymentMethodSerializer,HomeBannerSerializer
from django_filters.rest_framework import DjangoFilterBackend

class LoginView(APIView):
    def post(self, request):
        # Dummy login logic
        username = request.data.get('username')
        password = request.data.get('password')
        # Here you'd validate credentials and return a token or user data
        return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['user_id','name','email']
     # Or use custom permissions if needed



class SignupView(APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "message": "Signup successful",
                "user": UserSerializer(user).data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    class LoginView(APIView):
     def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            return Response({
                "message": "Login successful",
                "user": UserSerializer(user).data
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['gender', 'dob']

    def get_queryset(self):
        # Optional: restrict to current user's profile
        return UserProfile.objects.filter(user=self.request.user)

    def perform_update(self, serializer):
        # Ensure user can't change ownership
        serializer.save(user=self.request.user)

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', 'order_date']

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)




class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', 'product_type']

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', 'product_type']

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['notification_id','created_at']

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user)

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user']

    def get_queryset(self):
        return Blog.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['address','city','postal_code']

    def get_queryset(self):
        return Location.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['start_date', 'end_date']

    def get_queryset(self):
        return Offer.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



class PaymentMethodViewSet(viewsets.ModelViewSet):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['payment_id','account_number']

class HomeBannerViewSet(viewsets.ModelViewSet):
    queryset = HomeBanner.objects.all()
    serializer_class = HomeBannerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title']
    