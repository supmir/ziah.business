from django.db import models

# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=200, primary_key=True)
    def __str__(self):
        return self.category

class Product(models.Model):
    product_name = models.CharField(max_length=200, primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    img = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.product_name


class Content(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sequence = models.IntegerField()
    text = "text"
    photo = "photo"
    video = "video"
    content_types = [
        (text, "text"),
        (photo, "photo"),
        (video, "video"),
    ]
    content_type = models.CharField(max_length=200, choices=content_types)
    link = models.CharField(max_length=200)
    short_description = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.short_description
