from rest_framework.serializers import ModelSerializer
from authentification.models import User
 

class UserSerializer(ModelSerializer):
 
    def create(self, validated_data):
        """
        Create a user object, hash the password and make the user active before the creation.
        """
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.is_active = True
        user.save()
        return user

    class Meta:
        model = User
        fields = [
            'user_id',
            'first_name',
            'last_name',
            'email',
            'password']
