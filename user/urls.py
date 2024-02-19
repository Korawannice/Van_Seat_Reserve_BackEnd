from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import api
from rest_framework.routers import DefaultRouter
# from .views import UserViewSet

router = DefaultRouter()
# router.register(r'users', UserViewSet)

urlpatterns = [
    # path("me/", api.me, name="me"), 
    path("signup/", api.signup, name="signup"),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path('', include(router.urls)),
]
