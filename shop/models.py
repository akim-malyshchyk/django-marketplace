from django.db import models
from accounts.models import Customer


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE,
                                 related_name='orders',
                                 null=True,
                                 default=None)

    first_name = models.CharField(max_length=255, default='')
    last_name = models.CharField(max_length=255, default='')
    phone_number = models.CharField(max_length=15, default='')

    delivery_time = models.CharField(max_length=255, default='')
    delivery_address = models.CharField(max_length=255, default='')
    comment = models.CharField(max_length=255, default='')

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.created_at.ctime()


class Product(models.Model):
    orders = models.ManyToManyField(Order,
                                    through='ProductContainer',
                                    through_fields=('product', 'order'),
                                    related_name='goods'
                                    )
    name = models.CharField(max_length=255, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='goods')
    price = models.FloatField(default=0.0)

    def __str__(self):
        return self.name


class ProductContainer(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='cart')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
