from rest_framework.serializers import ModelSerializer
from softdesk_api.models import Project, Contributor


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
