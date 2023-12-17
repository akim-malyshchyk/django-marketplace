from shop.models import Category, Product, Order
from django.db.models import Sum, F
from django.core.mail import send_mail, mail_admins

from src import settings


class DatabaseService:
    @staticmethod
    def get_order(request):
        if request.user.is_authenticated:
            order = request.user.customer.orders.filter(is_confirmed=False).first()
            if order is None:
                order = request.user.customer.orders.create(customer=request.user.customer)
            return order
        elif 'order_id' in request.session:
            return Order.objects.get(pk=request.session['order_id'])

        order = Order.objects.create()
        request.session['order_id'] = order.id
        return order

    @staticmethod
    def set_product_quantity(order, product_id, quantity):
        cart = DatabaseService.get_cart(order)
        product_container = cart.filter(product_id=product_id).first()
        if product_container is not None:
            product_container.quantity = quantity
            product_container.save()

    @staticmethod
    def remove_product_from_order(order, product_id):
        cart = DatabaseService.get_cart(order)
        cart.filter(product_id=product_id).delete()

    @staticmethod
    def confirm_order(order, data):
        order.is_confirmed = True
        order.first_name = data['first_name']
        order.last_name = data['last_name']
        order.phone_number = data['phone_number']
        order.delivery_address = data['delivery_address']
        order.delivery_time = data['delivery_time']
        order.comment = data['comment']
        order.save()

    @staticmethod
    def get_cart(order):
        return order.cart.all()

    @staticmethod
    def get_categories():
        return Category.objects.all()

    @staticmethod
    def get_goods(category_id):
        return Product.objects.filter(category_id=category_id)

    @staticmethod
    def add_to_cart(order, product_id, quantity):
        cart = DatabaseService.get_cart(order)
        product_container = cart.filter(product_id=product_id).first()
        if product_container is None:
            cart.create(product_id=product_id, quantity=quantity, order=order)
        else:
            product_container.quantity += int(quantity)
            product_container.save()

    @staticmethod
    def get_order_price(order: Order):
        order_price = order.cart.annotate(container_price=F('quantity') * F('product__price')
                                          ).aggregate(Sum('container_price'))['container_price__sum']
        return order_price or 0

    @staticmethod
    def get_product(product_id):
        return Product.objects.get(pk=product_id)
