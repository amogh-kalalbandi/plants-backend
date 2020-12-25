from django.urls import path

from rest_framework_simplejwt import views as jwt_views
from apps.auth.views import MyTokenObtainPairView
from apps.auth.views import AuthLogoutAPIView

# List of all authentication APIs.
urlpatterns = [
    path('auth/login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/logout/', AuthLogoutAPIView.as_view(), name='auth_logout'),
]
