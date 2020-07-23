from django.contrib import admin

from .models import Product,Content,Category
# Register your models here.

admin.site.register(Product)
admin.site.register(Content)
admin.site.register(Category)