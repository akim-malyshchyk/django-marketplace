from django.contrib import admin
from shop.models import Category, Product, Order


class ProductAdminInline(admin.TabularInline):
    model = Product
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = (ProductAdminInline,)
    list_display = ('name', 'goods')

    @admin.display
    def goods(self, obj):
        return list(obj.goods.values_list('name', flat=True))


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'first_name', 'last_name', 'phone_number')

