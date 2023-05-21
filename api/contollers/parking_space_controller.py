from rest_framework import status
from api.auth import Auth
from api.contollers.user_controller import UserController
from api.serializers.parking_spaces import ParkingSpaceSerializer
from api.handlers.response_handler import ResponseHandler

class ParkingSpaceController():
    def store_parking_space(self, request):
        """
        Store parking space for a parking provider
        """
        parking_provider_id = Auth().extract_token(token=request.headers.get('Authorization').split("Bearer ")[1])['id']
        provider = UserController().get_user(id=parking_provider_id)
        request.data._mutable = True
        request.data['provider'] = provider['data']
        serializer = ParkingSpaceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return ResponseHandler(status=status.HTTP_201_CREATED, message='success').json_response()
        return ResponseHandler(status=status.HTTP_400_BAD_REQUEST, message=serializer.errors).json_response()