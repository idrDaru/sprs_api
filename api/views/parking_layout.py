from rest_framework.views import APIView
from rest_framework import status
from api.models.parking_layouts import ParkingLayout
from api.serializers.parking_layouts import ParkingLayoutSerializer
from api.handlers.response_handler import ResponseHandler

class ParkingLayoutDetails(APIView):
    """
    GET a parking layout details
    """
    def get(self, request, pk):
        parking_layout = ParkingLayout.objects.get(pk=pk)
        serializer = ParkingLayoutSerializer(parking_layout)
        return ResponseHandler(status=status.HTTP_200_OK, message='success', data=serializer.data).api_response()