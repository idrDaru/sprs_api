from rest_framework import status
from api.models.parking_spaces import ParkingSpace
from api.contollers.auth_controller import AuthenticationController
from api.contollers.user_controller import UserController
from api.serializers.parking_spaces import ParkingSpaceSerializer
from api.handlers.response_handler import ResponseHandler

class ParkingSpaceController():
    def get_all_parking_spaces(self, request):
        """
        GET all parking spaces
        """
        parking_spaces = ParkingSpace.objects.all()
        print(parking_spaces)
        serializer = ParkingSpaceSerializer(parking_spaces, many=True)
        return ResponseHandler(status=status.HTTP_200_OK, message='success', data=serializer.data).json_response()
    
    def store_parking_space(self, request):
        """
        Store parking space for a parking provider
        """
        parking_provider_id = AuthenticationController().extract_token(token=request.headers.get('Authorization').split("Bearer ")[1])['id']
        provider = UserController().get_user(id=parking_provider_id)
        request.data._mutable = True
        request.data['provider'] = provider['data']
        serializer = ParkingSpaceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return ResponseHandler(status=status.HTTP_201_CREATED, message='success').json_response()
        return ResponseHandler(status=status.HTTP_400_BAD_REQUEST, message=serializer.errors).json_response()
    
    def get_provider_parking_space(self, request):
        """
        Get parking space(s) based on provider id
        """
        parking_provider_id = AuthenticationController().extract_token(token=request.headers.get('Authorization').split("Bearer ")[1])['id']
        parking_space = ParkingSpace.objects.filter(provider_id = parking_provider_id).values()
        return ResponseHandler(status=status.HTTP_200_OK, message='success', data=parking_space).json_response()
    
    def get_parking_space_detail(self, pk):
        """
        Get a parking space detail based on parking space id
        """
        parking_space = ParkingSpace.objects.get(id=pk)
        serializer = ParkingSpaceSerializer(parking_space)
        return ResponseHandler(status=status.HTTP_200_OK, message='success', data=serializer.data).json_response()
    