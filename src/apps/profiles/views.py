from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model

from src.apps.profiles.serializers import UserSerializer

User = get_user_model()


class APIRegistrationView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
