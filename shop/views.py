from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET, require_POST

from shop.models import Category
from shop.utils import DatabaseService
from shop.forms import OrderForm


@require_GET
def main_page(request):
    return render(request, 'categories.html', context={'categories': DatabaseService.get_categories()})


@require_GET
def goods_category_view(request, category_id):
    category = Category.objects.get(pk=category_id)
    return render(request, 'goods.html', context={'category': category,
                                                  'goods': DatabaseService.get_goods(category_id)})


@require_GET
def order_view(request):
    order = DatabaseService.get_order(request)
    cart = DatabaseService.get_cart(order)
    price = DatabaseService.get_order_price(order)
    user = request.user
    if user.is_authenticated:
        initial = {'first_name': user.first_name,
                   'last_name': user.last_name,
                   'phone_number': user.customer.phone_number}
        return render(request, 'order.html', context={'cart': cart,
                                                      'price': price,
                                                      'form': OrderForm(initial=initial)})
    else:
        return render(request, 'order.html', context={'cart': cart, 'price': price, 'form': OrderForm()})


@require_POST
def add_to_cart_view(request, product_id):
    order = DatabaseService.get_order(request)
    product = DatabaseService.get_product(product_id)
    quantity = request.POST['quantity']
    DatabaseService.add_to_cart(order, product_id, quantity)
    messages.info(request, f'{product.name} (x{quantity}) was added to cart')
    return redirect('goods', category_id=product.category.id)


@require_POST
def set_product_quantity_view(request, product_id):
    order = DatabaseService.get_order(request)
    product = DatabaseService.get_product(product_id)
    quantity = request.POST['quantity']
    DatabaseService.set_product_quantity(order, product_id, quantity)
    messages.info(request, f'{product.name} quantity was changed to {quantity}')
    return redirect('order')


@require_POST
def remove_product_from_order_view(request, product_id):
    order = DatabaseService.get_order(request)
    product = DatabaseService.get_product(product_id)
    DatabaseService.remove_product_from_order(order, product_id)
    messages.info(request, f'{product.name} was removed from order')
    return redirect('order')


@require_POST
def confirm_order_view(request):
    order = DatabaseService.get_order(request)
    form = OrderForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        DatabaseService.confirm_order(order, cd)
        if not request.user.is_authenticated and 'order_id' in request.session:
            del request.session['order_id']
    else:
        messages.error(request, form.errors_prettified)
        return redirect('order')
    messages.success(request, 'Your order has been created successfully!')
    return redirect('main_page')
