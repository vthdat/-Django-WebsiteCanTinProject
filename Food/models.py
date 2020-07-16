from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Food(models.Model):

    BREAKFAST = 'BR'
    LUNCH = 'LU'
    DINNER = 'DI'
    BEVERAGE = 'BE'
    SNACK = 'SN'

    Food_Type_Choice = [
        (BREAKFAST, 'Bữa sáng'),
        (LUNCH, 'Bữa trưa'),
        (DINNER, 'Bữa tối'),
        (BEVERAGE, 'Đồ uống'),
        (SNACK, 'Ăn vặt'),
    ]

    food_name = models.CharField(max_length=100)
    food_type = models.CharField(max_length=2, choices=Food_Type_Choice, default=SNACK)
    description = models.TextField()
    price = models.FloatField(default=0)
    discount = models.FloatField(default=0)
    img = models.ImageField(upload_to='static/images/foods')
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify((str(self.id) + " " + self.food_name))
        super(Food, self).save(*args, **kwargs)

    def __str__(self):
        return self.food_name

    def get_absolute_url(self):
        return reverse('food:food_detail', args=[self.slug])
    
