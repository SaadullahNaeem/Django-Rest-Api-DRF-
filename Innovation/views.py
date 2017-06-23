from rest_framework import status, generics
from rest_framework.response import Response
from .form import *
from .serializers import *
from rest_framework.views import APIView


class Projects(APIView):

    def post(self, request):
        form = ProjectForm(request.data)
        if form.is_valid():
            form.save()
            return Response({'result': 'success'},
                            status=status.HTTP_200_OK)
        else:
            return Response({'errors': 'error'}, status=status.HTTP_200_OK)


class ProjectGet(generics.ListAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.all()


class CollaboratorCreate(APIView):

    def post(self, request):
        form = CollaborativeForm(request.data)
        if form.is_valid():
            form.save()
            return Response({'result': 'success'},
                            status=status.HTTP_200_OK)
        else:
            return Response({'errors': 'error'}, status=status.HTTP_200_OK)


class CollaboratorGet(generics.ListAPIView):
    serializer_class = CollaboratorSerializer

    def get_queryset(self):
        return Collaborator.objects.all()