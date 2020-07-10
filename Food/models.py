from django.db import models
from django.urls import reverse

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

    def __str__(self):
        return self.food_name

    def get_absolute_url(self):
        return reverse('food:food_detail', args=[self.id])
    
