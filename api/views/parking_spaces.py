from rest_framework.views import APIView
from rest_framework import status
from api.contollers.parking_space_controller import ParkingSpaceController
from api.handlers.response_handler import ResponseHandler
from api.models.parking_spaces import ParkingSpace
from api.serializers.parking_spaces import ParkingSpaceSerializer
from api.auth import Auth
    
class ParkingSpaceDetail(APIView):
    """
    Retrive, update, or delete a parking space based on id
    """
    def get(self, request, pk):
        parking_space = ParkingSpace.objects.get(id=pk)
        serializer = ParkingSpaceSerializer(parking_space)
        return ResponseHandler(status=status.HTTP_200_OK, message='success', data=serializer.data).api_response()
    
    def put(self, request, pk):
        """
        UPDATE parking space
        """
        parking_space = ParkingSpace.objects.get(pk=pk)
        serializer = ParkingSpaceSerializer(parking_space, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return ResponseHandler(status=status.HTTP_200_OK, message='success').api_response()
        return ResponseHandler(status=status.HTTP_400_BAD_REQUEST, message=serializer.errors, data=request.data).api_response()
    
class ParkingSpaceList(APIView):
    """
    GET all parking spaces
    """
    def get(self, request):
        parking_spaces = ParkingSpace.objects.all()
        serializer = ParkingSpaceSerializer(parking_spaces, many=True)
        return ResponseHandler(status=status.HTTP_200_OK, message="success", data=serializer.data).api_response()
    
class ParkingSpaceProvider(APIView):
    """
    GET, POST, PUT, DELETE parking space(s). Accessible only for ParkingSpace's owner(ParkingProvider)
    """
    def get(self, request):
        parking_provider_id = Auth().extract_token(token=request.headers.get('Authorization').split("Bearer ")[1])['id']
        parking_space = ParkingSpace.objects.filter(provider_id=parking_provider_id)
        serializer = ParkingSpaceSerializer(parking_space, many=True)
        return ResponseHandler(status=status.HTTP_200_OK, message="success", data=serializer.data).api_response()
    
    def post(self, request):
        parking_space = ParkingSpaceController().store_parking_space(request=request)
        return ResponseHandler(status=parking_space['status'], message=parking_space['message'], data=parking_space['data']).api_response()
    