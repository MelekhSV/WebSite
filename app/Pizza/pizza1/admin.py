from django.contrib import admin

# Register your models here.
from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductInBasket._meta.fields]
    list_filter = ('title',)
    search_fields = ['products_name']











admin.site.register(Post)





# class ProductAdmin (admin.ModelAdmin):
#     list_display = [field.name for field in ProductInBasket._meta.fields]
#
#     class Meta:
#         model = ProductInBasket
#
# admin.site.register(ProductInBasket, ProductAdmin)


admin.site.register(ProductInBasket, ProductAdmin)