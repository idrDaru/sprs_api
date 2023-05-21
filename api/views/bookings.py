from rest_framework.views import APIView
from rest_framework import status
from api.auth import Auth
from api.handlers.response_handler import ResponseHandler
from api.contollers.booking_controller import BookingController
from api.models.bookings import Booking
from api.serializers.bookings import BookingSerializer

class CreateBooking(APIView):
    def post(self, request, pk):
        """
        POST a booking by user
        """
        booking = BookingController().store_booking(request=request, parking_space_id=pk)
        return ResponseHandler(status=booking['status'], message=booking['message'], data=booking['data']).api_response()
    
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

    