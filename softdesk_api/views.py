from rest_framework.viewsets import ModelViewSet
from softdesk_api.serializers import (
    ProjectSerializer, 
    ProjectDetailSerializer, 
    ContributorSerializer, 
    IssuesSerializer,
    CommentSerializer)
from authentification.models import User
from softdesk_api.models import Project, Contributor, Issue, Comment
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class ProjectViewset(ModelViewSet):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    detail_serializer_class = ProjectDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Get all the projects that the current user authentified created.        
        """
        queryset = Project.objects.filter(author_user_id=self.request.user.user_id)
        return queryset

    def get_serializer_class(self):
        """
        Every action will use a detail serializer except the listing of all the projects.
        """
        if self.action != 'list':
            return self.detail_serializer_class
        return super().get_serializer_class()

class ContributorViewset(ModelViewSet):

    serializer_class = ContributorSerializer
    permission_classes = [IsAuthenticated]

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

    def create(self, request, project_pk="project_pk"):
        contributor_data = request.data
        user_id = User.objects.get(user_id=request.data['user_id'])
        project_id = Project.objects.get(project_id=project_pk)
        contributor_data['project_id'] = project_id
        contributor_data['user_id'] = user_id
        contributor = Contributor.objects.create(**contributor_data)
        contributor.save()
        serializer = ContributorSerializer(contributor)
        return Response(serializer.data)

    def destroy(self, request, project_pk, pk):
        contributor = Contributor.objects.get(id=pk)
        contributor.delete()
        return Response()

class IssueViewset(ModelViewSet):
    
    queryset = Issue.objects.all()
    serializer_class = IssuesSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        project_id = self.kwargs.get('project_pk')
        queryset = Issue.objects.filter(project_id=project_id)
        return queryset
    
    def create(self, request, project_pk="project_pk"):
        assignee_user_pk = request.data['assignee_user_id']
        project_id = Project.objects.get(project_id=project_pk)
        assignee_user_id = User.objects.get(user_id=assignee_user_pk)
        author_user_id = User.objects.get(user_id=self.request.user.user_id)
        issue_data = request.data
        issue_data['project_id'] = project_id
        issue_data['assignee_user_id'] = assignee_user_id
        issue_data['author_user_id'] = author_user_id
        issue = Issue.objects.create(**issue_data)
        issue.save()
        serializer = IssuesSerializer(issue)
        return Response(serializer.data)

class CommentViewset(ModelViewSet):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        issue_id = self.kwargs.get('issue_pk')
        queryset = Comment.objects.filter(issue_id=issue_id)
        return queryset
    
    def create(self, request, project_pk="project_pk", issue_pk="issue_pk"):
        comment_data = request.data
        author_user_id = User.objects.get(user_id=self.request.user.user_id)
        issue_id = Issue.objects.get(id=issue_pk)
        comment_data['author_user_id'] = author_user_id
        comment_data['issue_id'] = issue_id
        comment = Comment.objects.create(**comment_data)
        comment.save()
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
