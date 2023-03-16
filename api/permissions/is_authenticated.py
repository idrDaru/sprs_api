from rest_framework import permissions
from api.contollers.auth_controllers import AuthenticationController
import jwt


class IsAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        auth = request.headers.get('Authorization')
        
        if auth is None:
            return False
        
        try:
            AuthenticationController().extract_token(auth.split("Bearer ")[1])
        except jwt.ExpiredSignatureError:
            return False
        except jwt.InvalidSignatureError:
            return False
        return True