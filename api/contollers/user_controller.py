from rest_framework import status
from api.handlers.response_handler import ResponseHandler
from api.models.parking_users import ParkingUser
from api.models.parking_providers import ParkingProvider
from api.serializers.users import UserSerializer
from api.serializers.parking_users import ParkingUserSerializer
from api.serializers.parking_providers import ParkingProviderSerializer

class UserController():
    def get_user(self, id):
        try:
            parking_user = ParkingUser.objects.get(id=id)
            serializer = ParkingUserSerializer(parking_user)
            return ResponseHandler(status=status.HTTP_200_OK, message="sucess", data=serializer.data).json_response()
        except ParkingUser.DoesNotExist:
            pass

        try:
            parking_provider = ParkingProvider.objects.get(id=id)
            serializer = ParkingProviderSerializer(parking_provider)
            return ResponseHandler(status=status.HTTP_200_OK, message="success", data=serializer.data).json_response()
        except ParkingProvider.DoesNotExist:
            pass
        
        return ResponseHandler(status=status.HTTP_404_NOT_FOUND, message="User Not Found").json_response()
    
