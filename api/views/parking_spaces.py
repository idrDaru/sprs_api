from rest_framework.views import APIView
from api.contollers.parking_space_controller import ParkingSpaceController
from api.handlers.response_handler import ResponseHandler
    
class ParkingSpaceDetail(APIView):
    """
    Retrive, update, or delete a parking space based on id
    """
    def get(self, request, pk):
        # Get a parking space based on id
        parking_space = ParkingSpaceController().get_parking_space_detail(pk=pk)
        return ResponseHandler(status=parking_space['status'], message=parking_space['message'], data=parking_space['data']).api_response()
    
class ParkingSpaceList(APIView):
    """
    GET all parking spaces
    """
    def get(self, request):
        parking_spaces = ParkingSpaceController().get_all_parking_spaces(request=request)
        return ResponseHandler(status=parking_spaces['status'], message=parking_spaces['message'], data=parking_spaces['data']).api_response()
    
class ParkingSpaceProvider(APIView):
    """
    GET, POST, PUT, DELETE parking space(s). Accessible only for ParkingSpace's owner(ParkingProvider)
    """
    def get(self, request, pk):
        parking_space = ParkingSpaceController().get_provider_parking_space(request=request)
        return ResponseHandler(status=parking_space['status'], message=parking_space['message'], data=parking_space['data']).api_response()
    
    def post(self, request, pk):
        parking_space = ParkingSpaceController().store_parking_space(request=request)
        return ResponseHandler(status=parking_space['status'], message=parking_space['message'], data=parking_space['data']).api_response()
    
    def put(self, request, pk):
        return
    
    def delete(self, request, pk):
        return
    