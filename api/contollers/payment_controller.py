from rest_framework import status
from api.handlers.response_handler import ResponseHandler
from api.models.payment_methods import PaymentMethod
from api.serializers.payment_methods import PaymentMethodSerializer
from api.contollers.user_controller import UserController
from api.contollers.auth_controller import AuthenticationController

class PaymentController():
    def store_payment_method(self, request):
        """
        Store payment method for a user
        """
        parking_user_id = AuthenticationController().extract_token(token=request.headers.get('Authorization').split("Bearer ")[1])['id']
        user = UserController().get_user(id=parking_user_id)
        request.data._mutable = True
        request.data['user'] = user['data']
        serializer = PaymentMethodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return ResponseHandler(status=status.HTTP_201_CREATED, message='success').json_response()
        return ResponseHandler(status=status.HTTP_400_BAD_REQUEST, message=serializer.error_messages).json_response()

    def get_payment_method(self, request):
        """
        Get payment method based on user id
        """
        parking_user_id = AuthenticationController().extract_token(token=request.headers.get('Authorization').split("Bearer ")[1])['id']
        payment_method = PaymentMethod.objects.filter(user_id=parking_user_id).values()
        return ResponseHandler(status=status.HTTP_200_OK, message='success', data=payment_method).json_response()