from django.urls import path
from .views import *
from . import views

app_name = 'food'

urlpatterns = [
    path('<str:slug>/', FoodDetailView.as_view(), name='food_detail'),
    path('', FoodListView.as_view(), name='menu'),
    path('bua-sang', FoodBreakfastListView.as_view(), name='bua-sang'),
    path('bua-trua', FoodLunchListView.as_view(), name='bua-trua'),
    path('bua-toi', FoodDinnerListView.as_view(), name='bua-toi'),
    path('do-uong', FoodBeverageListView.as_view(), name='do-uong'),
    path('an-vat', FoodSnackListView.as_view(), name='an-vat'),
]