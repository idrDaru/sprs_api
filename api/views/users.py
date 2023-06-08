from api.models.users import User
from rest_framework.views import APIView
from rest_framework import status
from api.auth import Auth
from api.contollers.user_controller import UserController
from api.handlers.response_handler import ResponseHandler
from api.permissions.is_authenticated import IsAuthenticated
from api.serializers.users import UserSerializer
from api.serializers.parking_users import ParkingUserSerializer
from api.serializers.parking_providers import ParkingProviderSerializer
from api.models.parking_users import ParkingUser
from api.models.parking_providers import ParkingProvider


class UserDetail(APIView):
    """
    Retrieve, update or delete a user instance
    """
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user_id = Auth().extract_token(token=request.headers.get('Authorization').split("Bearer ")[1])['id']
        try: 
            parking_user = ParkingUser.objects.get(id=user_id)
            serializer = ParkingUserSerializer(parking_user)
            return ResponseHandler(status=status.HTTP_200_OK, message="success", data=serializer.data).api_response()
        except ParkingUser.DoesNotExist:
            pass

        try:
            parking_provider = ParkingProvider.objects.get(id=user_id)
            serializer = ParkingProviderSerializer(parking_provider)
            return ResponseHandler(status=status.HTTP_200_OK, message="success", data=serializer.data).api_response()
        except ParkingProvider.DoesNotExist:
            pass

        return ResponseHandler(status=status.HTTP_404_NOT_FOUND, message="User Not Found").api_response()
    
    def put(self, request):
        request_data = Auth().extract_token(token=request.headers.get('Authorization').split("Bearer ")[1])
        if request_data['type'] == 1:
            user = ParkingUser.objects.get(pk=request_data['id'])
            parking_user_serializer = ParkingUserSerializer(user, data=request.data)
            if parking_user_serializer.is_valid():
                parking_user_serializer.save()
                userr = User.objects.get(pk=parking_user_serializer.data['user']['id'])
                user_serializer = UserSerializer(userr, data=request.data)
                if user_serializer.is_valid():
                    user_serializer.save()
                return ResponseHandler(status=status.HTTP_200_OK, message="success").api_response()
            return ResponseHandler(status=status.HTTP_400_BAD_REQUEST, message=parking_provider_serializer.errors).api_response()
        
        if request_data['type'] == 2:
            user = ParkingProvider.objects.get(pk=request_data['id'])
            parking_provider_serializer = ParkingProviderSerializer(user, data=request.data)
            if parking_provider_serializer.is_valid():
                parking_provider_serializer.save()
                userr = User.objects.get(pk=parking_provider_serializer.data['user']['id'])
                user_serializer = UserSerializer(userr, data=request.data)
                if user_serializer.is_valid():
                    user_serializer.save()
                return ResponseHandler(status=status.HTTP_200_OK, message="success").api_response()
            return ResponseHandler(status=status.HTTP_400_BAD_REQUEST, message=parking_provider_serializer.errors).api_response()


        return ResponseHandler(status=status.HTTP_400_BAD_REQUEST, message="User Not Found").api_response()