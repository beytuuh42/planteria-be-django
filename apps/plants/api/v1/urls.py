from django.urls import path
from . import views

urlpatterns = [
    path('plants', views.plant_list, name="plant_list"),
    path('plants/<int:plant_id>', views.plant_detail, name="plant_detail"),
    path('plants/<int:plant_id>/images',
         views.plant_images, name="plant_images"),
]
