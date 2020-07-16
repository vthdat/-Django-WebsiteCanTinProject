from django.urls import path
from .views import ArticleListView, ArticleDetailView

app_name='articles'

urlpatterns = [
    path('<str:slug>/', ArticleDetailView.as_view(), name='detail'),
    path('', ArticleListView.as_view(), name='list'),

]