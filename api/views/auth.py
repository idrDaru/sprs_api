from rest_framework.views import APIView
from api.auth import Auth
from api.handlers.response_handler import ResponseHandler
from api.models.users import User
from api.models.parking_users import ParkingUser
from api.models.parking_providers import ParkingProvider
from api.serializers.users import UserSerializer
from api.serializers.parking_users import ParkingUserSerializer
from api.serializers.parking_providers import ParkingProviderSerializer
from rest_framework import status

class Register(APIView):
    def post(self, request):
        """
        User register functionality
        """
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            if request.data.get("type", None) is not None:
                request.data['user'] = serializer.data
                parking_provider_serializer = ParkingProviderSerializer(data=request.data)
                if parking_provider_serializer.is_valid():
                    parking_provider_serializer.save()
                    return ResponseHandler(status=status.HTTP_201_CREATED, message="success").api_response()
                instance.delete()
                return ResponseHandler(status=status.HTTP_400_BAD_REQUEST, message=parking_provider_serializer.errors).api_response()
            
            request.data['user'] = serializer.data
            parking_user_serializer = ParkingUserSerializer(data=request.data)
            if parking_user_serializer.is_valid():
                parking_user_serializer.save()
                return ResponseHandler(status=status.HTTP_201_CREATED, message="success").api_response()
            instance.delete()
            return ResponseHandler(status=status.HTTP_400_BAD_REQUEST, message=parking_user_serializer.errors).api_response()
        # user = AuthenticationController().register(data=request.data)
        return ResponseHandler(status=status.HTTP_400_BAD_REQUEST, message=serializer.errors).api_response()
    
class Login(APIView):
    def post(self, request):
        """
        Handle user login
        """
        try:
            user = User.objects.get(email=request.data['email'])
        except User.DoesNotExist:
            return ResponseHandler(status=status.HTTP_404_NOT_FOUND, message="user not found", data=request.data).api_response()
        
        serializer = UserSerializer(user)
        if request.data['password'] != serializer.data['password']:
            return ResponseHandler(status=status.HTTP_401_UNAUTHORIZED, message="unauthorized").api_response()
        
        try:
            parking_user = ParkingUser.objects.get(user_id=user.id)
            serializer = ParkingUserSerializer(parking_user)
            payload = {
                'id': serializer.data['id'],
                'type': serializer.data['user']['type'],
            }
            token = Auth().create_token(data=payload)
            return_data = {
                'access_token': token,
            }

            return ResponseHandler(status=status.HTTP_200_OK, message="success", data=return_data).api_response()
        except ParkingUser.DoesNotExist:
            pass

        try:
            parking_provider = ParkingProvider.objects.get(user_id=user.id)
            serializer = ParkingProviderSerializer(parking_provider)
            payload = {
                'id': serializer.data['id'],
                'type': serializer.data['user']['type'],
            }
            token = Auth.create_token(self, data=payload)
            return_data = {
                'access_token': token,
            }
            return ResponseHandler(status=status.HTTP_200_OK, message="success", data=return_data).api_response()
        except ParkingProvider.DoesNotExist:
            pass

        return ResponseHandler(status=status.HTTP_404_NOT_FOUND, message="user not found").api_response()
    

