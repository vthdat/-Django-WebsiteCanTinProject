from decimal import Decimal
from django.conf import settings
from Food.models import Food

class Cart(object):
    def __init__(self, request):
        """
        Initialize the cart.
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
        # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, food, quantity=1, override_quantity=False):
        """
        Add a product to the cart or update its quantity.
        """
        food_id = str(food.id)
        if food_id not in self.cart:
            self.cart[food_id] = {'quantity': 0,
                                  'price': str(food.price)}
        if override_quantity:
            self.cart[food_id]['quantity'] = quantity
        else:
            self.cart[food_id]['quantity'] += quantity
            self.save()

    def save(self):
        # mark the session as "modified" to make sure it gets saved
        self.session.modified = True

    def remove(self, food):
        food_id = str(food.id)
        if food_id in self.cart:
            del self.cart[food_id]
            self.save()

    def __iter__(self):
        """
        Iterate over the items in the cart and get the products
        from the database.
        """
        food_ids = self.cart.keys()
        # get the product objects and add them to the cart
        foods = Food.objects.filter(id__in=food_ids)
        cart = self.cart.copy()
        for food in foods:
            cart[str(food.id)]['food'] = food
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """
        Count all items in the cart.
        """
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        # remove cart from session
        del self.session[settings.CART_SESSION_ID]
        self.save()