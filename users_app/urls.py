from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SignupView, LoginView, UserViewSet
from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet
from .views import OrderViewSet
from .views import CartViewSet, FavoriteViewSet, NotificationViewSet
from .views import BlogViewSet, LocationViewSet, OfferViewSet
from .views import PaymentMethodViewSet,HomeBannerViewSet
from .views import SignupView, LoginView,UserViewSet


router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'profiles', UserProfileViewSet, basename='userprofile')
router.register(r'orders', OrderViewSet, basename='order')
router.register(r'cart', CartViewSet, basename='cart')
router.register(r'favorite', FavoriteViewSet, basename='favorite')
router.register(r'notifications', NotificationViewSet, basename='notifications')
router.register(r'blogs', BlogViewSet, basename='blogs')
router.register(r'locations', LocationViewSet, basename='locations')
router.register(r'offers', OfferViewSet, basename='offers')
router.register(r'payment-methods', PaymentMethodViewSet)
router.register(r'home-banners', HomeBannerViewSet)





urlpatterns = [
     path('', include(router.urls)),
     path('signup/', SignupView.as_view(), name='signup'),
     path('login/', LoginView.as_view(), name='login'),    
]

