from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Food

# Create your views here.

class FoodListView(ListView):
    model = Food
    template_name = 'food_list.html'

class FoodDetailView(DetailView):
    model = Food
    template_name = 'food_detail.html'