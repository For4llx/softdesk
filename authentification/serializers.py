from rest_framework.serializers import ModelSerializer
from authentification.models import User
 

class SignUpSerializer(ModelSerializer):
 
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'password']


class LoginSerializer(ModelSerializer):
 
    class Meta:
        model = User
        fields = ['id','email', 'password']