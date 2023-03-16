from django.http.request import QueryDict
from rest_framework import status
from api.handlers.response_handler import ResponseHandler
from api.models.users import User
from api.models.parking_users import ParkingUser
from api.models.parking_providers import ParkingProvider
from api.serializers.users import UserSerializer
from api.serializers.parking_users import ParkingUserSerializer
from api.serializers.parking_providers import ParkingProviderSerializer


class UserController():
    def get_user(self, id):
        try:
            parking_user = ParkingUser.objects.get(id=id)
            serializer = ParkingUserSerializer(parking_user)
            return ResponseHandler(status=status.HTTP_200_OK, message="sucess", data=serializer.data).json_response()
        except ParkingUser.DoesNotExist:
            pass

        try:
            parking_provider = ParkingProvider.objects.get(id=id)
            serializer = ParkingProviderSerializer(parking_provider)
            return ResponseHandler(status=status.HTTP_200_OK, message="success", data=serializer.data).json_response()
        except ParkingProvider.DoesNotExist:
            pass
        
        return ResponseHandler(status=status.HTTP_404_NOT_FOUND, message="User Not Found").json_response()
    
    def get_user_reverse(self, user_id):
        try:
            parking_user = ParkingUser.objects.get(user_id=user_id)
            serializer = ParkingUserSerializer(parking_user)
            return ResponseHandler(status=status.HTTP_200_OK, message="sucess", data=serializer.data).json_response()
        except ParkingUser.DoesNotExist:
            pass

        try:
            parking_provider = ParkingProvider.objects.get(user_id=user_id)
            serializer = ParkingProviderSerializer(parking_provider)
            return ResponseHandler(status=status.HTTP_200_OK, message="success", data=serializer.data).json_response()
        except ParkingProvider.DoesNotExist:
            pass
        
        return ResponseHandler(status=status.HTTP_404_NOT_FOUND, message="User Not Found").json_response()
    
    def store_user(self, data):
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            # Save User data using UserSerializer
            instance = serializer.save()
            # Check if "type" data provided from request
            if data.get("type", None) is not None:
                # Call function to store parking parking provider data
                store_parking_provider = self.__store_parking_provider(data=data, user=serializer.data)
                if store_parking_provider['status'] is not 201:
                    instance.delete()
                return ResponseHandler(status=store_parking_provider['status'], message=store_parking_provider['message'], data=store_parking_provider['data']).json_response()
            # Call function to store parking user data
            store_parking_user = self.__store_parking_user(data=data, user=serializer.data)
            if store_parking_user['status'] is not 201:
                instance.delete()
            return ResponseHandler(status=store_parking_user['status'], message=store_parking_user['message'], data=store_parking_user['data']).json_response()
            
        return ResponseHandler(status=status.HTTP_400_BAD_REQUEST, message=serializer.errors).json_response()

    def __store_parking_user(self, data, user):
        data._mutable = True
        data['user'] = user
        serializer = ParkingUserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return ResponseHandler(status=status.HTTP_201_CREATED, message="success", data=serializer.data).json_response()
        return ResponseHandler(status=status.HTTP_400_BAD_REQUEST, message=serializer.errors, data=serializer.data).json_response()

    def __store_parking_provider(self, data, user):
        data._mutable = True
        data['user'] = user
        serializer = ParkingProviderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return ResponseHandler(status=status.HTTP_201_CREATED, message="success").json_response()
        return ResponseHandler(status=status.HTTP_400_BAD_REQUEST, message=serializer.errors, data=serializer.data).json_response()