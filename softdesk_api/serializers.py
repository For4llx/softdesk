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

    def get_user(self):
        """
        Get the current user authentified.
        """
        user = self.context.get("request").user
        return user

    def create(self, validated_data):
        """
        Create a project object, the author of the project
        will be the current user authentified.
        """
        user = self.get_user()
        validated_data['author_user_id'] = user
        project = super().create(validated_data)
        project.save()
        return project


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
