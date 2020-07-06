from django.shortcuts import render
from django.views.generic import TemplateView
from Food.models import Food

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'new_home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['food_list'] = Food.objects.all()
        return context
    