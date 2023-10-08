from django.db import models

# Create your models here.

class Merchant(models.Model):
    merchant_id   = models.CharField(max_length=255, primary_key=True)

    merchant_name = models.CharField(max_length=255)
    rating        = models.FloatField()
    response_rate = models.FloatField()
    joined        = models.IntegerField()
    no_products   = models.IntegerField()
    response_time = models.CharField(max_length=50)
    followers     = models.IntegerField()

    def __str__(self):
        return self.name

class Product(models.Model):
    product_id   = models.CharField(max_length=255, primary_key=True)
    merchant_id  = models.ForeignKey(
        Merchant,
        on_delete=models.PROTECT,
        default=None
    )

    product_name = models.CharField(max_length=255)
    preferred    = models.BooleanField()
    mall         = models.BooleanField()
    avg_rating   = models.FloatField()
    total_rating = models.IntegerField()
    total_sold   = models.IntegerField()
    price        = models.FloatField()
    fav_count    = models.IntegerField()
    qty_avail    = models.IntegerField()
    description  = models.TextField()
    img_src      = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Review(models.Model):
    review_id   = models.CharField(max_length=255, primary_key=True)
    customer_id = models.ForeignKey(
        Customer,
        on_delete=models.PROTECT,
        default=None
    )
    merchant_id  = models.ForeignKey(
        Merchant,
        on_delete=models.PROTECT,
        default=None
    )
    product_id  = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        default=None
    )

    date    = models.DateTimeField()
    rating  = models.FloatField()
    content = models.TextField()

    def __str__(self):
        return self.name


class Customer(models.Model):
    user_name = models.CharField(max_length=255, primary_key=True)

    no_reviews   = models.IntegerField()
    review_list  = models.JSONField()
    no_products  = models.IntegerField()
    product_dict = models.JSONField()
    mean_rating  = models.FloatField()

    
    def __str__(self):
        return self.name