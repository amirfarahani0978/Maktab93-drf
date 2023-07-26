from django.db import models

# Create your models here.
# class Category(models.Model):
#     name = models.CharField(max_length=100)

class Product(models.Model):
    name = models.CharField(max_length=100)
    price_confirm = models.IntegerField()
    price = models.IntegerField()
    def __str__(self) -> str:
        return self.name
class Comment(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    product_id = models.ForeignKey(Product , on_delete=models.CASCADE , related_name='products')

    def __str__(self) -> str:
        return self.title
