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

class FoodBreakfastListView(ListView):
    model = Food
    template_name = 'custom_food_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['food_list'] = Food.objects.filter(food_type='BR')
        return context

class FoodLunchListView(ListView):
    model = Food
    template_name = 'custom_food_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['food_list'] = Food.objects.filter(food_type='LU')
        return context

class FoodDinnerListView(ListView):
    model = Food
    template_name = 'custom_food_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['food_list'] = Food.objects.filter(food_type='DI')
        return context

class FoodBeverageListView(ListView):
    model = Food
    template_name = 'custom_food_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['food_list'] = Food.objects.filter(food_type="BE")
        return context

class FoodSnackListView(ListView):
    model = Food
    template_name = 'custom_food_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['food_list'] = Food.objects.filter(food_type='SN')
        return context

    