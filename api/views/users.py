from rest_framework.views import APIView
from api.contollers.user_controller import UserController
from api.handlers.response_handler import ResponseHandler

class UserDetail(APIView):
    """
    Retrieve, update or delete a user instance
    """
    def get(self, request):
        # Return either parking user or parking provider data
        user = UserController().get_user(id=request.data['id'])
        return ResponseHandler(status=user['status'], message=user['message'], data=user['data']).api_response()
    
    def delete(self, request):
        # Delete one Parking User or Parking Provider
        return True
    
    def put(self, request):
        # Update one Parking User or Parking Provider data
        return True