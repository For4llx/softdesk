from rest_framework.serializers import ModelSerializer
from authentification.models import User
 

class SignupSerializer(ModelSerializer):
 
    class Meta:
        model = User
        fields = [
            'user_id',
            'first_name',
            'last_name',
            'email',
            'password'
        ]
