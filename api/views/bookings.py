from rest_framework.views import APIView
from rest_framework import status
from api.auth import Auth
from api.handlers.response_handler import ResponseHandler
from api.contollers.booking_controller import BookingController
from api.contollers.user_controller import UserController
from api.contollers.parking_space_controller import ParkingSpaceController
from api.models.bookings import Booking
from api.models.parking_spaces import ParkingSpace
from api.serializers.bookings import BookingSerializer
from api.serializers.parking_spaces import ParkingSpaceSerializer

class CreateBooking(APIView):
    def post(self, request):
        """
        POST a booking by user
        """
        parking_user_id = Auth().extract_token(token=request.headers.get('Authorization').split("Bearer ")[1])['id']
        user = UserController().get_user(id=parking_user_id)
        parking_space = ParkingSpace.objects.get(id=request.data['parking_space_id'])
        parking_space_serializer = ParkingSpaceSerializer(parking_space)
        request.data['user'] = user['data']
        request.data['parking_space'] = parking_space_serializer.data
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return ResponseHandler(status=status.HTTP_201_CREATED, message='success').api_response()
        return ResponseHandler(status=status.HTTP_400_BAD_REQUEST, message=serializer.errors, data=serializer.data).api_response()
    
class UserBooking(APIView):
    def get(self, request):
        """
        GET user's booking(s)
        """
        parking_user_id = Auth().extract_token(token=request.headers.get('Authorization').split("Bearer ")[1])['id']
        bookings = Booking.objects.filter(user_id=parking_user_id)
        serializer = BookingSerializer(bookings, many=True)
        return ResponseHandler(status=status.HTTP_200_OK, message="success", data=serializer.data).api_response()
    
class BookingDetail(APIView):
    def get(self, request, pk):
        """
        Retrieve one booking
        """
        booking = Booking.objects.get(pk=pk)
        serializer = BookingSerializer(booking)
        return ResponseHandler(status=status.HTTP_200_OK, message='success', data=serializer.data).api_response()

    