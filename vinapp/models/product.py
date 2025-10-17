from django.db import models
from .category import Category

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField()
    category = models.ForeignKey("Category", on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to="image/") # stored inside MEDIA_ROOT/images/

    @staticmethod
    def get_all_products():
        return Product.objects.all()