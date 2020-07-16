from django.shortcuts import render
from django.views.generic import TemplateView
from Food.models import Food
from cart.forms import CartAddFoodForm
from cart.cart import Cart

# Create your views here.

class HomePageView(TemplateView):
    model = Food
    template_name = 'new_home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_product_form'] = CartAddFoodForm()
        context['food_list'] = Food.objects.exclude(food_type='BE')[:6]
        context['beverage_list'] = Food.objects.filter(food_type='BE')[:6]
        return context

class AboutPageView(TemplateView):
    template_name = 'about.html'

class ContactPageView(TemplateView):
    template_name = 'contact.html'
    