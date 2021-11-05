from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly

from apps.core.serializers import ChooseSerializerClassMixin

from .models import User
from .permissions import IsAdmin
from .serializers import CreateUserSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action in ["list"]:
            self.permission_classes = [IsAdmin]
        return super().get_permissions()
