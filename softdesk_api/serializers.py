from rest_framework.serializers import ModelSerializer
from softdesk_api.models import Project, Contributor, Issue, Comment


class ProjectSerializer(ModelSerializer):
 
    class Meta:
        model = Project
        fields = ['project_id', 'title']

class ProjectDetailSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class ContributorSerializer(ModelSerializer):
    class Meta:
        model = Contributor
        fields = '__all__'

class IssuesSerializer(ModelSerializer):
    class Meta:
        model = Issue
        fields = '__all__'

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
