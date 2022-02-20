from django.contrib import admin

from application.product.models import Category, Product

admin.site.register(Category)
admin.site.register(Product)
