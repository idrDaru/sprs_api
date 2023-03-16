from rest_framework.views import APIView
from api.contollers.auth_controllers import AuthenticationController
from api.handlers.response_handler import ResponseHandler

class Register(APIView):
    def post(self, request):
        """
        User register functionality
        """
        user = AuthenticationController().register(data=request.data)
        return ResponseHandler(status=user['status'], message=user['message'], data=user['data']).api_response()
    
class Login(APIView):
    def post(self, request):
        """
        Handle user login
        """
        user = AuthenticationController().login(data=request.data)
        return ResponseHandler(status=user['status'], message=user['message'], data=user['data']).api_response()
    

