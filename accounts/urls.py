from django.urls import path
from .views import (
    RegisterUserAPIView,
    UserProfileAPIView,
    CustomTokenObtainPairView
)
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', RegisterUserAPIView.as_view(),
         name='register'),
    path('profile/', UserProfileAPIView.as_view(),
         name='user-profile'),
    path('login/', CustomTokenObtainPairView.as_view(),
         name='custom_token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
]
