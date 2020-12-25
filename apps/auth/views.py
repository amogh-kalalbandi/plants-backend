"""Api file for handling authentications."""

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.auth.auth_process_functions import AuthProcessFunctions
from apps.utils.constants import ResponseConstants


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Set custom claims for the JWT tokens."""

    @classmethod
    def get_token(cls, user):
        """Return JWT access and refresh tokens on validation."""
        token = super().get_token(user)

        token['last_login'] = str(user.last_login)
        # token['first_login'] = user.is_first_login

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class AuthLogoutAPIView(APIView):
    """AuthLogoutAPIView API View."""

    def post(self, request):
        """Post method to change the last login time of user."""
        resp_status = status.HTTP_200_OK
        data = AuthProcessFunctions.logout_process_function(request.user)
        if data[ResponseConstants.ERROR_KEY.value]:
            resp_status = status.HTTP_400_BAD_REQUEST

        return Response(data, status=resp_status)
