from datetime import datetime, timedelta
from rest_framework import status
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
        """
        return jwt.decode(token, env('SECRET_KEY'), algorithm="HS256").get('data')