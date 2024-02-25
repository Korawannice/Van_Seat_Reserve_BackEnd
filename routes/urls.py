from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RoutesViewSet,AddRoutesViewSet

router = DefaultRouter()
router.register(r'routes', RoutesViewSet)
router.register(r'addroutes', AddRoutesViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
