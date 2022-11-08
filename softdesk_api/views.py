from rest_framework.viewsets import ModelViewSet
from softdesk_api.serializers import (
    ProjectSerializer, 
    ProjectDetailSerializer, 
    ContributorSerializer, 
    IssuesSerializer)
from softdesk_api.models import Project, Contributor, Issue
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


class ContributorViewset(ModelViewSet):

    serializer_class = ContributorSerializer

    def get_queryset(self):
        """
        Get a contributor from a project OR get all contributors from a project
        """
        project_id = self.kwargs.get('project_pk')
        contributor_id = self.kwargs.get('pk')
        if contributor_id:
            queryset = Contributor.objects.get(id=contributor_id)
        else:
            queryset = Contributor.objects.filter(project_id=project_id)
        return queryset

class IssueViewset(ModelViewSet):
    
    queryset = Issue.objects.all()
    serializer_class = IssuesSerializer

    def get_queryset(self):
        project_id = self.kwargs.get('project_pk')
        queryset = Issue.objects.filter(project_id=project_id)
        return queryset
