from rest_framework import viewsets
from .models import Routes, AddRoutes
from .serializer import RoutesSerializer, AddRoutesSerializer
from rest_framework.response import Response
from rest_framework import status

class RoutesViewSet(viewsets.ModelViewSet):
    queryset = Routes.objects.all()
    serializer_class = RoutesSerializer
    
class AddRoutesViewSet(viewsets.ModelViewSet):
    queryset = AddRoutes.objects.all()
    serializer_class = AddRoutesSerializer
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
