from datetime import datetime, timedelta
from rest_framework import status
from api.models.users import User
from api.models.parking_users import ParkingUser
from api.models.parking_providers import ParkingProvider
from api.serializers.users import UserSerializer
from api.serializers.parking_users import ParkingUserSerializer
from api.serializers.parking_providers import ParkingProviderSerializer
from api.handlers.response_handler import ResponseHandler
from api.contollers.user_controller import UserController
import jwt, os, environ

class AuthenticationController():
    global env
    env = environ.Env(
        # set casting, default value
        DEBUG=(bool, False)
    )

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

    def register(self, data):
        """
        Handle User Registration
        """
        store_user = UserController().store_user(data=data)
        return ResponseHandler(status=store_user['status'], message=store_user['message'], data=store_user['data']).json_response()
    
    def login(self, data):
        """
        Handle User Login
        """
        try:
            user = User.objects.get(email=data['email'])
        except User.DoesNotExist:
            return ResponseHandler(status=status.HTTP_404_NOT_FOUND, message="user not found", data=data).json_response()
        
        user_serializer = UserSerializer(user)
        if data['password'] != user_serializer.data['password']:
            return ResponseHandler(status=status.HTTP_401_UNAUTHORIZED, message="unauthorized").json_response()
        
        user_data = UserController().get_user_reverse(user_id=user.id)
        
        payload = {
            'id': user_data['data']['id'],
            'type': user_data['data']['user']['type'],
        }

        token = self.__create_token__(data=payload)

        return_data = {
            'access_token': token,
        }

        return ResponseHandler(status=status.HTTP_200_OK, message="success", data=return_data).json_response()

    
    def __create_token__(self, data):
        """
        Create JWT Token
        """
        payload = {
            'data': data,
            'exp': datetime.now() + timedelta(days=1)
        }
        token = jwt.encode(payload, env('SECRET_KEY'), algorithm="HS256")

        return token
    
    def extract_token(self, token):
        """
        Extract JWT Token
        # """
        return jwt.decode(token, env('SECRET_KEY'), algorithms="HS256").get('data')