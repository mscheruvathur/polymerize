from rest_framework import status
from rest_framework.views import APIView
from api.controller.rest_response import RestResponse
from api.controller.user_controller import UserController
from api.serializer.user_serializer import UserRegistrationSerializer, UserUpdationSerializer

class EmployeeAPIView(APIView):
    
    response = RestResponse
    controller = UserController()

    def post (self, request):
        try:
            serialized_user = UserRegistrationSerializer(data=request.data)
            if serialized_user.is_valid():
                user = serialized_user.create()
                authcode = self.controller.generate_auth_code(user)
                return self.response({
                    "success" : "User registration successful",
                    "authcode" : authcode
                    }, status=status.HTTP_201_CREATED)
            return self.response({
                "error" : serialized_user.errors
            }, status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return self.response({
                "error": "Internal server error",
                "message" : str(e)
                }, status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put (self, request) :
        try: 
            serialized_user = UserUpdationSerializer(data=request.data)
            if serialized_user.is_valid():
                user = self.controller.update(**serialized_user._validated_data)
                return self.response({
                    "success" : "User updation successfull"
                }, status.HTTP_200_OK)
            return self.response({
                "error" : serialized_user.errors
            }, status.HTTP_400_BAD_REQUEST)
        except Exception as  e:
            return self.response({
                "error": "Internal server error",
                "message" : str(e)
                }, status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete (self, request, pk = None) :
        try: 
            if pk:
                self.controller.delete(pk)
                return self.response({
                    "success" : "User removed successfully"
                }, status.HTTP_200_OK)
            return self.response({
                "error" : "Not a vlid user"
            }, status.HTTP_400_BAD_REQUEST)
        except Exception as  e:
            return self.response({
                "error": "Internal server error",
                "message" : str(e)
                }, status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get (self, request, pk = None) :
        try: 
            pass
        except Exception as  e:
            return self.response({
                "error": "Internal server error",
                "message" : str(e)
                }, status.HTTP_500_INTERNAL_SERVER_ERROR)