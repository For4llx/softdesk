from rest_framework.viewsets import ModelViewSet
from softdesk_api.serializers import ProjectSerializer, ProjectDetailSerializer, ContributorSerializer
from authentification.serializers import UserSerializer
from softdesk_api.models import Project, Contributor
from authentification.models import User
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


class ProjectViewset(ModelViewSet):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    detail_serializer_class = ProjectDetailSerializer

    def get_queryset(self):
        user_id = self.request.GET.get('user_id')
        if user_id:
            queryset = Project.objects.filter(author_user_id=user_id)
            return queryset
        return super().get_queryset()

    def get_serializer_class(self):
        if self.action == 'retrieve' or self.action == 'create' or self.action == 'update':
            return self.detail_serializer_class
        return super().get_serializer_class()
    
    @action(detail=True, methods=['get', 'post'], queryset=Contributor, serializer_class=ContributorSerializer)
    def users(self, request, pk=None):
        if request.method == 'POST':
            contributor = ContributorSerializer(data=request.data)
            if contributor.is_valid():
                contributor.save()
                return Response(contributor.data, status.HTTP_201_CREATED)
        if request.method == 'GET':
            users = Contributor.objects.filter(project_id=pk)
            serializer = self.get_serializer(users, many=True)
            return Response(serializer.data, status.HTTP_200_OK)









"""
    if request.method == 'GET':
    def get_queryset(self):
    contributors = Contributor.objects.filter(project_id=pk)
    return contributors
    return Response(contributors)
    elif request.method == 'POST':
    new_contributor = ContributorSerializer(data=request.data)
    new_contributor.save()
"""
  