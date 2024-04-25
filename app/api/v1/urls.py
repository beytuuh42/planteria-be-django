from django.urls import path, include
from . import views

urlpatterns = [
    path('plants', views.plant_list),
    path('plants/<int:id>', views.plant_detail),
    path('plants/<int:plant_id>/images', views.plant_images),
    path('auth/register', views.register),
    path('auth/login', views.login),
    path('auth/logout', views.logout),
    path('user', views.user),
]