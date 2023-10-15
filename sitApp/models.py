from django.db import models

# Create your models here.


class Merchant(models.Model):
    class Meta:
        app_label = 'sitApp'

    # Primary Key
    merchant_id           = models.CharField(max_length=255, primary_key=True)

    # Initial data features
    merchant_name         = models.CharField(max_length=255, null=True)
    total_rating          = models.FloatField(null=True)
    response_rate_percent = models.FloatField(null=True)
    days                  = models.IntegerField(null=True)
    no_products           = models.IntegerField(null=True)
    response_speed        = models.CharField(max_length=50, null=True)
    no_follower           = models.IntegerField(null=True)

    def __str__(self):
        return self.merchant_id

class Product(models.Model):
    class Meta:
        app_label = 'sitApp'

    # Primary and Foreign Key
    product_id   = models.CharField(max_length=255, primary_key=True)
    merchant_id  = models.ForeignKey(
        Merchant,
        on_delete=models.PROTECT,
        default=None
    )

    # Initial data features
    category     = models.CharField(max_length=50, null=True)
    product_name = models.CharField(max_length=255, null=True)
    avg_rating   = models.FloatField(null=True)
    total_rating = models.IntegerField(null=True)
    total_sold   = models.IntegerField(null=True)
    price        = models.FloatField(null=True)
    fav_count    = models.IntegerField(null=True)
    qty_avail    = models.IntegerField(null=True)
    description  = models.TextField(null=True)
    img_src      = models.CharField(max_length=255, null=True)

    # Subsequent new features
    avg_norm_rating   = models.FloatField(null=True)
    count_norm_rating = models.IntegerField(null=True)
    merchant_class    = models.CharField(max_length=50, null=True)
    credibility_score = models.IntegerField(null=True)
    pos_1             = models.CharField(max_length=20, null=True)
    pos_2             = models.CharField(max_length=20, null=True)
    pos_3             = models.CharField(max_length=20, null=True)
    neg_1             = models.CharField(max_length=20, null=True)
    neg_2             = models.CharField(max_length=20, null=True)
    neg_3             = models.CharField(max_length=20, null=True)


    def __str__(self):
        return self.product_id

class User(models.Model):
    class Meta:
        app_label = 'sitApp'

    # Primary Key
    username          = models.CharField(max_length=255, primary_key=True)

    # Initial data features
    no_review         = models.IntegerField(null=True)
    review_list       = models.TextField(null=True)
    no_product        = models.IntegerField(null=True)
    product_dict      = models.TextField(null=True)
    mean_rating       = models.FloatField(null=True)

    # Subsequent new features
    min_dist_username = models.CharField(max_length=255, null=True)

    
    def __str__(self):
        return self.username
    
class Review(models.Model):
    class Meta:
        app_label = 'sitApp'

    # Primary and Foreign Key
    review_id   = models.CharField(max_length=255, primary_key=True)
    username   = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        default=None
    )
    product_id  = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        default=None
    )

    # Initial data features
    date = models.CharField(max_length=50, null=True)
    rating = models.FloatField(null=True)
    content = models.TextField(null=True)
    location = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.review_id
