from rest_framework.views import APIView
from rest_framework import status
from api.models.parking_locations import ParkingLocation
from api.serializers.parking_locations import ParkingLocationSerializer
from api.handlers.response_handler import ResponseHandler

class ParkingLocationList(APIView):
    """
    GET all parking locations
    """
    def get(self, request):
        parking_locaions = ParkingLocation.objects.all()
        serializer = ParkingLocationSerializer(parking_locaions, many=True)
        return ResponseHandler(status=status.HTTP_200_OK, message='success', data=serializer.data).api_response()



