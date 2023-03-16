from rest_framework.views import APIView
from api.contollers.user_controller import UserController
from api.contollers.auth_controllers import AuthenticationController
from api.handlers.response_handler import ResponseHandler
from api.permissions.is_authenticated import IsAuthenticated

class UserDetail(APIView):
    """
    Retrieve, update or delete a user instance
    """
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user_id = AuthenticationController().extract_token(token=request.headers.get('Authorization').split("Bearer ")[1])['id']
        # Return either parking user or parking provider data
        user = UserController().get_user(id=user_id)
        return ResponseHandler(status=user['status'], message=user['message'], data=user['data']).api_response()
    
    def delete(self, request):
        # Delete one Parking User or Parking Provider
        return True
    
    def put(self, request):
        # Update one Parking User or Parking Provider data
        return True