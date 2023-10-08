from django.db import models

# Create your models here.

class Customer(models.Model):
    user_id   = models.CharField(max_length=255, primary_key=True)
    user_name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Merchant(models.Model):
    merchant_id   = models.CharField(max_length=255, primary_key=True)
    merchant_name = models.CharField(max_length=255)

    user_id       = models.ForeignKey(
        Customer,
        on_delete=models.PROTECT,
        default=None
    )

    def __str__(self):
        return self.name

class Product(models.Model):
    product_id   = models.CharField(max_length=255, primary_key=True)
    product_name = models.CharField(max_length=255)

    merchant_id  = models.ForeignKey(
        Customer,
        on_delete=models.PROTECT,
        default=None
    )

    def __str__(self):
        return self.name

class Review(models.Model):
    review_id   = models.CharField(max_length=255, primary_key=True)
    review_text = models.TextField()

    customer_id = models.ForeignKey(
        Customer,
        on_delete=models.PROTECT,
        default=None
    )

    product_id  = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        default=None
    )

class Data(models.Model):


    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.first_name


