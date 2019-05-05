from django.contrib import admin
from .models import Images, Category, Brand, Product, Review
# Register your models here.

admin.site.register(Images)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Review)
