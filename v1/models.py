from django.db import models

# Create your models here.


class Product(models.Model):
    product_name = models.CharField(max_length=200, primary_key=True)
    maxxima = "maxxima"
    garden = "garden"
    product_categories = [
        (maxxima, "maxxima"),
        (garden, "garden"),
    ]
    product_category = models.CharField(
        max_length=200, choices=product_categories)
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
