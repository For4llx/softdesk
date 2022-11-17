from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from authentification.models import User
from authentification.serializers import UserSerializer


class SignupViewset(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
