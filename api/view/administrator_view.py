from rest_framework import status
from rest_framework.views import APIView
from api.controller.rest_response import RestResponse
from api.serializer.administrator_serializer import AdministratorRegistrationSerializer
from api.controller.user_controller import UserController

class AdministratorAPIView(APIView) :

    response = RestResponse
    controller = UserController()

    def post (self, request):
        try:
            serialized_data = AdministratorRegistrationSerializer(data= request.data)
            if serialized_data.is_valid():
                administrator = serialized_data.create()
                authcode = self.controller.generate_auth_code(administrator= administrator)
                return self.response({
                    "success": "Administrator created successfuly",
                    "authcode" : authcode
                }, status.HTTP_201_CREATED)
            return self.response({
                "error": serialized_data.errors
            }, status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return self.response({
                "error" : "Internal server error",
                "message" : str(e)
            }, status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put (self, request):
        try:
            pass
        except Exception as e:
            return self.response({
                "error" : "Internal server error",
                "message" : str(e)
            }, status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete (self, request):
        try:
            pass
        except Exception as e:
            return self.response({
                "error" : "Internal server error",
                "message" : str(e)
            }, status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get (self, request):
        try:
            pass
        except Exception as e:
            return self.response({
                "error" : "Internal server error",
                "message" : str(e)
            }, status.HTTP_500_INTERNAL_SERVER_ERROR)

class AdministratorLoginAPIView(APIView) :

    response = RestResponse

    def post (self, request):
        try:
            pass
        except Exception as e:
            return self.response({
                "error" : "Internal server error"
            }, status.HTTP_500_INTERNAL_SERVER_ERROR)