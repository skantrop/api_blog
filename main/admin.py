from django.contrib import admin
from .models import Category, Product, Review, Order, OrderItems
from account.models import User

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(User)

