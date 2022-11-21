from rest_framework.views import APIView
from api.controller.rest_response import RestResponse
from rest_framework import status
from api.controller.user_controller import UserController
from api.controller.token.token_generator import AdministratorToken



class AdministratorTokenAPIView(APIView) :
    
    response = RestResponse
    controller = UserController()

    def post( self ,request):
        try:
            if 'auth_code' in request.data:
                print(request.data['auth_code'])
                auth_instance = self.controller.verify_auth_code(request.data['auth_code'])
                _token = AdministratorToken()
                self.controller.expir_auth_code(request.data['auth_code'])
                tokens = _token.create_tokens(administrator=auth_instance.administrator)
                response = self.response({
                    "success": {"access_token": tokens.access_token}
                }, status.HTTP_201_CREATED)
                response.set_cookie('refresh_token', tokens.refresh_token,
                    httponly=True, samesite=None)
                return response
            return self.response({
                "error": "auth code not found"
            }, status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return self.response({
                "error" : "Internal server error"
            }, status.HTTP_500_INTERNAL_SERVER_ERROR)