from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article

# Create your views here.



class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles_list'] = Article.objects.order_by('-date')
        return context

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'