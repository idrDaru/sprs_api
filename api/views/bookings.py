from rest_framework.views import APIView
from api.handlers.response_handler import ResponseHandler
from api.contollers.booking_controller import BookingController

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
        booking = BookingController().get_user_booking(request=request)
        return ResponseHandler(status=booking['status'], message=booking['message'], data=booking['data']).api_response()
    