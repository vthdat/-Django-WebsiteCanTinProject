from django.urls import path
from .views import FoodListView, FoodDetailView

urlpatterns = [
    path('<int:pk>/', FoodDetailView.as_view(), name='food_detail'),
    path('', FoodListView.as_view(), name='food_list'),
]