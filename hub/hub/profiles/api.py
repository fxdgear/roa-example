from django.contrib.auth import authenticate, login as auth_login

from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework import exceptions
from rest_framework.views import APIView
from rest_framework.response import Response

from profiles.models import DockerUser
from profiles.serializers import DockerUserSerializer


class DockerUserViewSet(viewsets.ModelViewSet):
    queryset = DockerUser.objects.all()
    serializer_class = DockerUserSerializer


class LoginView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        """
        User Login end point.

        This endpoint accepts either a legacy password (hashed using phpass) or
        a new password that has been hashed using the django hashing algorithm.

        If the password used, is a phpass, it'll attempt to validate it, and
        then convert the password to use the django hashing algorithm.

        Login endpoint returns a serialized user object, along with 2 access
        tokens.

        """
        username = self.request.DATA.get('username', None)
        password = self.request.DATA.get('password', None)
        user = authenticate(username=username, password=password)
        if user is None:
            raise exceptions.AuthenticationFailed(
                'Unable to login with provided credentials.'
            )

        serializer = DockerUserSerializer(instance=user)
        auth_login(request, user)
        return Response(serializer.data)
