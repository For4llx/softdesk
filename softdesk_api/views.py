from rest_framework.viewsets import ModelViewSet
from softdesk_api.serializers import (
    ProjectSerializer, 
    ProjectDetailSerializer, 
    ContributorSerializer, 
    IssuesSerializer,
    CommentSerializer)
from softdesk_api.models import Project, Contributor, Issue, Comment


class ProjectViewset(ModelViewSet):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    detail_serializer_class = ProjectDetailSerializer

    def get_queryset(self):
        user_id = self.request.GET.get('user_id')
        queryset = Project.objects.filter(author_user_id=user_id)
        return queryset

    def get_serializer_class(self):
        if self.action != 'list':
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

class CommentViewset(ModelViewSet):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        issue_id = self.kwargs.get('issue_pk')
        queryset = Comment.objects.filter(issue_id=issue_id)
        return queryset