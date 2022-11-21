from rest_framework.views import APIView
from rest_framework import status
from api.controller.rest_response import RestResponse
from api.serializer.project_serializer import ProjectCreationSerializer

class ProjectAPIView (APIView) :

    response = RestResponse

    def post (self, request, pk = None) :
        try: 
            serialized_project = ProjectCreationSerializer(data= request.data)
            if serialized_project.is_valid():
                serialized_project.save()
                return self.response({
                    "success", "Project created successfully"
                }, status.HTTP_201_CREATED)
            return self.response({
                "error" : serialized_project.errors
            }, status.HTTP_400_BAD_REQUEST)
        except Exception as  e:
            return self.response({
                "error": "Internal server error",
                "message" : str(e)
                }, status.HTTP_500_INTERNAL_SERVER_ERROR)
    