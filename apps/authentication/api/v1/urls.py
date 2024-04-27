from . import views
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path('auth/register', views.register),
    path('auth/logout', views.logout),
    path('auth/login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/login/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/login/verify', TokenVerifyView.as_view(), name='token_verify'),
]
