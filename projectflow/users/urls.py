from django.urls import path
from .views import RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('users/register/', RegisterView.as_view(), name='register'),
    path('users/login/', TokenObtainPairView.as_view(), name='login'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]