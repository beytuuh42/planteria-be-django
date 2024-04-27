from django.urls import path, include
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('plants', views.plant_list),
    path('plants/<int:id>', views.plant_detail),
    path('plants/<int:plant_id>/images', views.plant_images),
    path('auth/register', views.register),
    path('auth/login', views.login),
    path('auth/logout', views.logout),
    path('auth/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]
