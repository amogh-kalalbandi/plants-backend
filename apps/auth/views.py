from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


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
