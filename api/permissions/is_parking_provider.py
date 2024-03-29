from rest_framework import permissions
from api.auth import Auth
import jwt

class IsParkingProvider(permissions.BasePermission):
    def has_permission(self, request, view):
        auth = request.headers.get('Authorization')
        
        if auth is None:
            return False
        
        try:
            payload = Auth().extract_token(auth.split("Bearer ")[1])
            if payload['type'] is not 2:
                return False
        except jwt.ExpiredSignatureError:
            return False
        except jwt.InvalidSignatureError:
            return False
        
        return True