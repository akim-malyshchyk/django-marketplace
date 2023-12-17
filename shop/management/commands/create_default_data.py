import random

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

from accounts.utils import create_customer
from shop.models import Category, Product


class Command(BaseCommand):
    help = 'Create categories, goods, superuser account, users with random usernames'

    def handle(self, *args, **options) -> None:
        """
        Create categories, goods, superuser account, users with random usernames
        """
        password = 'pass1234'
        username = 'admin'
        mail = 'admin@test.com'

        User = get_user_model()
        user = User.objects.create_superuser(username, mail, password)
        create_customer(user, '+111111111111')

        for i in range(5):
            username = get_random_string(length=12)
            user = User.objects.create_user(username=username, email=f'{username}@test.com', password='pwd12345')
            create_customer(user, f'+1{random.randint(10000000, 100000000)}')

        for category_name in ['drinks', 'grocery', 'bakery', 'jewelery', 'toys', 'sports inventory']:
            Category.objects.create(name=category_name)

        category1, category2, category3, category4, category5, category6 = Category.objects.all().order_by('id')

        for product_name in ['juice', 'water', 'milk', 'beer', 'wine']:
            Product.objects.create(name=product_name, price=random.randint(200, 500) / 100, category=category1)

        for product_name in ['orange', 'lemon', 'tangerine', 'tomato', 'potato', 'cucumber']:
            Product.objects.create(name=product_name, price=random.randint(200, 500) / 100, category=category2)

        for product_name in ['bread', 'cake', 'muffin', 'cookies', 'croissants', 'baguettes', 'doughnut']:
            Product.objects.create(name=product_name, price=random.randint(200, 500) / 100, category=category3)

        for product_name in ['bracelet', 'brooch', 'costume', 'earring', 'gem', 'glass', 'gold']:
            Product.objects.create(name=product_name, price=random.randint(20000, 500000) / 100, category=category4)

        for product_name in ['doll', 'plaything', 'trinket', 'bauble', 'curio', 'game', 'knickknack', 'novelty']:
            Product.objects.create(name=product_name, price=random.randint(1000, 5000) / 100, category=category5)

        for product_name in ['bicycle', 'football ball', 'basketball ball', 'sneakers']:
            Product.objects.create(name=product_name, price=random.randint(2000, 50000) / 100, category=category6)
