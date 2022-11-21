from rest_framework.views import APIView
from rest_framework import status
from api.controller.rest_response import RestResponse
from api.serializer.company_serializer import CompanyCreationSerializer

class CompanyAPIView (APIView) :

    response = RestResponse

    def post (self, request, pk = None) :
        try: 
            serialized_company = CompanyCreationSerializer(data= request.data)
            if serialized_company.is_valid():
                serialized_company.save()
                return self.response({
                    "success" : "Company created successfully"
                }, status.HTTP_201_CREATED)
            return self.response({
                "error" : serialized_company.errors
            }, status.HTTP_400_BAD_REQUEST)
        except Exception as  e:
            return self.response({
                "error": "Internal server error",
                "message" : str(e)
                }, status.HTTP_500_INTERNAL_SERVER_ERROR)
    