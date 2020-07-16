from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    photo = models.ImageField(upload_to='static/images/articles')
    slug = models.SlugField(unique=True, blank=True, null=True, max_length=100)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse('articles:detail', args=[str(self.slug)])