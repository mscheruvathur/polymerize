from rest_framework import status
from rest_framework.views import APIView
from api.controller.rest_response import RestResponse
from api.serializer.admin_serializer import AdminRegistrationSerializer
from api.controller.user_controller import UserController

class AdminAPIView(APIView) :

    response = RestResponse
    controller = UserController()

    def post (self, request):
        try:
            serialized_admin = AdminRegistrationSerializer(data= request.data)
            if serialized_admin.is_valid():
                admin = serialized_admin.create()
                authcode = self.controller.generate_auth_code(admin=admin)
                return self.response({
                    "success" : "Admin created successfully",
                    "authcode" : authcode
                }, status.HTTP_201_CREATED)
            return self.response({
                "error" : serialized_admin.errors
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