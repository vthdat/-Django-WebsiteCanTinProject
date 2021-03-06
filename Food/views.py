from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Food
from cart.forms import CartAddFoodForm
from cart.cart import Cart

# Create your views here.

class FoodListView(ListView):
    model = Food
    template_name = 'food_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['beverage_list'] = Food.objects.filter(food_type='BE')
        context['breakfast_list'] = Food.objects.filter(food_type='BR')
        context['lunch_list'] = Food.objects.filter(food_type='LU')
        context['dinner_list'] = Food.objects.filter(food_type='DI')
        context['snack_list'] = Food.objects.filter(food_type='SN')
        context['cart_product_form'] = CartAddFoodForm()
        return context

class FoodDetailView(DetailView):
    model = Food
    template_name = 'food_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['food_list'] = Food.objects.filter(food_type=self.object.food_type).exclude(id=self.object.id)
        context['cart_product_form'] = CartAddFoodForm()
        return context

class FoodBreakfastListView(ListView):
    model = Food
    template_name = 'custom_food_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['food_list'] = Food.objects.filter(food_type='BR')
        context['cart_product_form'] = CartAddFoodForm()
        return context

class FoodLunchListView(ListView):
    model = Food
    template_name = 'custom_food_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['food_list'] = Food.objects.filter(food_type='LU')
        context['cart_product_form'] = CartAddFoodForm()
        return context

class FoodDinnerListView(ListView):
    model = Food
    template_name = 'custom_food_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['food_list'] = Food.objects.filter(food_type='DI')
        context['cart_product_form'] = CartAddFoodForm()
        return context

class FoodBeverageListView(ListView):
    model = Food
    template_name = 'custom_food_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['food_list'] = Food.objects.filter(food_type='BE')
        context['cart_product_form'] = CartAddFoodForm()
        return context

class FoodSnackListView(ListView):
    model = Food
    template_name = 'custom_food_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['food_list'] = Food.objects.filter(food_type='SN')
        context['cart_product_form'] = CartAddFoodForm()
        return context

    