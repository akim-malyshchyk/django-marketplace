from django.urls import path


from shop.views import (
    goods_category_view,
    order_view,
    add_to_cart_view,
    set_product_quantity_view,
    confirm_order_view,
    remove_product_from_order_view,
)

urlpatterns = [
    path('category/<int:category_id>', goods_category_view, name='goods'),
    path('order', order_view, name='order'),
    path('add_to_cart/<int:product_id>', add_to_cart_view, name='add_to_cart'),
    path('set_product_quantity/<int:product_id>', set_product_quantity_view, name='set_product_quantity'),
    path('remove_product/<int:product_id>', remove_product_from_order_view, name='remove_product'),
    path('confirm_order', confirm_order_view, name='confirm_order')
]
