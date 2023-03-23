from rest_framework import status
from api.handlers.response_handler import ResponseHandler
from api.models.bookings import Booking
from api.serializers.bookings import BookingSerializer
from api.contollers.auth_controller import AuthenticationController
from api.contollers.user_controller import UserController
from api.contollers.parking_space_controller import ParkingSpaceController

class BookingController():
    def get_user_booking(self, request):
        """
        GET user's booking(s)
        """
        parking_user_id = AuthenticationController().extract_token(token=request.headers.get('Authorization').split("Bearer ")[1])['id']
        booking = Booking.objects.filter(user_id=parking_user_id).values()
        return ResponseHandler(status=status.HTTP_200_OK, message='success', data=booking).json_response()

    def store_booking(self, request, parking_space_id):
        """
        POST a new booking made by user
        """
        parking_user_id = AuthenticationController().extract_token(token=request.headers.get('Authorization').split("Bearer ")[1])['id']
        user = UserController().get_user(id=parking_user_id)
        parking_space = ParkingSpaceController().get_parking_space_detail(pk=parking_space_id)
        request.data._mutable = True
        request.data['user'] = user['data']
        request.data['parking_space'] = parking_space['data']
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return ResponseHandler(status=status.HTTP_201_CREATED, message='success').json_response()
        return ResponseHandler(status=status.HTTP_400_BAD_REQUEST, message=serializer.errors, data=serializer.data).json_response()