from rest_framework.views import APIView
from api.contollers.payment_controller import PaymentController
from api.handlers.response_handler import ResponseHandler
from api.permissions.is_authenticated import IsAuthenticated

class PaymentMethod(APIView):
    """
    Retrieve, update or delete a payment method for/of a user
    """
    permission_classes = [IsAuthenticated]
    def get(self, request):
        # Get user's payment method
        payment_method = PaymentController().get_payment_method(request=request)
        return ResponseHandler(status=payment_method['status'], message=payment_method['message'], data=payment_method['data']).api_response()

    def post(self, request):
        # Add user's payment method
        payment_method = PaymentController().store_payment_method(request=request)
        return ResponseHandler(status=payment_method['status'], message=payment_method['message'], data=payment_method['data']).api_response()