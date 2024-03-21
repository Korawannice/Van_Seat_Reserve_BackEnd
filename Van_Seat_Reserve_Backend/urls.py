from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    path('add_van/', views.RetrieveUpdateDestroyDriveRouteView.as_view({
        "post": "create",
    }), name='add_van'),
    path('remove_van/<int:pk>/', views.RetrieveUpdateDestroyDriveRouteView.as_view({
        'delete': 'destroy'
    }), name='remove_van'),
    path('van_list/', views.ListCreateDriveRouteView.as_view({
        'get': 'list'
    }), name='van_list'),
    path('list_locations/', views.ListLocations.as_view(), name='list_locations'),
    path('driver_response/', views.ListDriverResponse.as_view(),
         name='driver_response'),
    path('create_reservation/', views.CreateReservationAndViewTicket.as_view(),
         name='create_reservation'),
    path('list_reservation/', views.ListCreateVanReservationView.as_view(), name='list_reservation'),
    path('mark-reservation-as-successful/<str:number_of_ticket>/',
         views.MarkReservationAsSuccessful.as_view(), name='mark-reservation-as-successful'),
    path('qr-code-to-ticket-verification/<int:pk>/',
         views.QrCodeToTicketVerification.as_view(), name='qr-code-to-ticket-verification'),
    path('search-van-driver/', views.SearchVanDriver.as_view(), name='search-van-driver'),
]
