from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    photo = models.ImageField(upload_to='static/images/articles')

    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])