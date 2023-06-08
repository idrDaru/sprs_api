from django.urls import path
from api.views import *

urlpatterns = [
    # Authentication URL -- DONE
    path('api/register/', Register.as_view()), 
    path('api/login/', Login.as_view()),

    # Parking Space URL
    path('api/parking-spaces/', ParkingSpaceList.as_view()),
    path('api/parking-space/<str:pk>', ParkingSpaceDetail.as_view()),
    path('api/parking-space-provider/', ParkingSpaceProvider.as_view()),

    # Booking URL
    path('api/create-booking/', CreateBooking.as_view()),
    path('api/user-booking/', UserBooking.as_view()),
    path('api/booking/<str:pk>', BookingDetail.as_view()),
    path('api/pay-booking/<str:pk>', PayBooking.as_view()),

    # User URL
    path('api/user/', UserDetail.as_view()),

    # Payment URL
    path('api/payment-method/', PaymentMethod.as_view()),

    # Parking Location URL
    path('api/parking-locations/', ParkingLocationList.as_view()),
    path('api/parking-location/<str:pk>', ParkingLocationDetails.as_view()),

    # Parking Layout URL
    path('api/parking-layout/<str:pk>', ParkingLayoutDetails.as_view())
]