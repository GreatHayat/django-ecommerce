from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Images(models.Model):
    title = models.CharField(max_length = 64, blank=True, null=True)
    image = models.ImageField(upload_to="photos/")
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.title}"


class Category(models.Model):
    name = models.CharField(max_length=128, blank=False)
    image = models.ForeignKey(Images, on_delete=models.CASCADE, related_name="images")
    tagline = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.name}"

class Brand(models.Model):
    name = models.CharField(max_length=64, blank=False)
    category = models.ManyToManyField(Category)
    
    def __str__(self):
        return f"{self.name}"

class Product(models.Model):
    name = models.CharField(max_length=128, blank=False)
    category = models.ManyToManyField(Category)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="categories")
    image = models.ImageField(upload_to="photos/")
    related_images = models.ManyToManyField(Images)
    original_price = models.DecimalField(max_digits=6, decimal_places=2)
    discount_percentage = models.IntegerField(blank=True, null=True)
    discount_price = models.DecimalField(max_digits=6, decimal_places = 2, blank=True, null=True)
    inStock = models.BooleanField(default=True)
    isFeatured = models.BooleanField(default=False)
    isPromotion = models.BooleanField(default=False)
    warrenty = models.IntegerField()
    description = models.TextField()


    def __str__(self):
        return f"{self.name}"

class Review(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    username = models.CharField(max_length=64)
    title = models.CharField(max_length=32)
    message = models.TextField()

    def __str__(self):
        return f"{self.username} - {self.title}"