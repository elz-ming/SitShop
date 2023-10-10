from django.db import models

# Create your models here.

class Merchant(models.Model):
    merchant_id = models.CharField(max_length=255, primary_key=True)

    merchant_name = models.CharField(max_length=255, null=True)
    rating = models.FloatField(null=True)
    response_rate = models.FloatField(null=True)
    joined = models.IntegerField(null=True)
    no_products = models.IntegerField(null=True)
    response_time = models.CharField(max_length=50, null=True)
    followers = models.IntegerField(null=True)

    def __str__(self):
        return self.merchant_id


class Product(models.Model):
    product_id = models.CharField(max_length=255, primary_key=True)
    merchant_id = models.ForeignKey(
        Merchant,
        on_delete=models.PROTECT,
        default=None
    )

    product_name = models.CharField(max_length=255, null=True)
    preferred = models.BooleanField(null=True)
    mall = models.BooleanField(null=True)
    avg_rating = models.FloatField(null=True)
    total_rating = models.IntegerField(null=True)
    total_sold = models.IntegerField(null=True)
    price = models.FloatField(null=True)
    fav_count = models.IntegerField(null=True)
    qty_avail = models.IntegerField(null=True)
    description = models.TextField(null=True)
    img_src = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.product_id


class Customer(models.Model):
    user_name = models.CharField(max_length=255, primary_key=True)

    no_reviews = models.IntegerField(null=True)
    review_list = models.JSONField(null=True)
    no_products = models.IntegerField(null=True)
    product_dict = models.JSONField(null=True)
    mean_rating = models.FloatField(null=True)

    def __str__(self):
        return self.user_name


class Review(models.Model):
    review_id = models.CharField(max_length=255, primary_key=True)
    user_name = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        default=None
    )

    merchant_id = models.ForeignKey(
        Merchant,
        on_delete=models.PROTECT,
        default=None
    )
    product_id = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        default=None
    )

    date = models.DateTimeField(null=True)
    rating = models.FloatField(null=True)
    content = models.TextField(null=True)

    def __str__(self):
        return self.review_id

class Data(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(default=0)



    def __str__(self):
        return self.first_name


