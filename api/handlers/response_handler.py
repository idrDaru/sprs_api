from rest_framework.response import Response

class ResponseHandler:
    def __init__(self, status=None, message=None, data=None):
        self.status = status
        self.message = message
        self.data = data
    
    def api_response(self):
        return Response(status=self.status, data=self.json_response())
    
    def json_response(self):
        json_data = {
            'status': self.status,
            'message': self.message,
            'data': self.data,
        }

        return json_data