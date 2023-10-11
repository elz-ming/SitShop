import os
import sys
import django
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sitProject.settings')
django.setup()

import pandas as pd
from sitApp.models import Merchant, Product, User, Review
from django.db import IntegrityError

merchant_df = pd.read_csv("./sitData/asset/etlMerchant.csv")
product_df  = pd.read_csv("./sitData/asset/etlProduct.csv")
user_df     = pd.read_csv("./sitData/asset/etlUser.csv")
review_df   = pd.read_csv("./sitData/asset/etlReview.csv")

def input_merchant():
    for index, merchant in merchant_df.iterrows():
        try:
            Merchant.objects.create(
                merchant_id           = merchant['merchant_id'],
                merchant_name         = merchant['name'],
                total_rating          = merchant['total_rating'],
                response_rate_percent = merchant['response_rate_percent'],  
                days                  = merchant['days'],
                no_products           = merchant['no_products'],
                response_speed        = merchant['response_speed'],
                no_follower           = merchant['no_follower']
            )
        
        except IntegrityError:
            pass

def input_product():
    for index, product in product_df.iterrows():
        try:
            merchant = Merchant.objects.get(merchant_id=product['merchant_id'])

            Product.objects.create(
                product_id            = product['product_id'],
                merchant_id           = merchant,

                category              = product['category'],
                product_name          = product['name'],
                avg_rating            = product['avg_rating'],
                total_rating          = product['total_rating'],
                total_sold            = product['total_sold'],
                price                 = product['price'],
                fav_count             = product['fav_count'],
                qty_avail             = product['qty_avail'],
                description           = product['description'],
                img_src               = product['img_src']
            )
        
        except IntegrityError:
            pass

def input_user():
    for index, user in user_df.iterrows():
        try:
            User.objects.create(
                username     = user['username'],
                no_review    = user['no_review'],
                review_list  = user['review_id'],
                no_product   = user['no_product'],
                product_dict = user['product_id'],
                mean_rating  = user['mean_rating']
            )
        
        except IntegrityError:
            pass

def input_review():
    for index, review in review_df.iterrows():
        try:
            user    = User.objects.get(username=review['username'])
        except:
            user    = None

        try:
            product = Product.objects.get(product_id=review['product_id'])
        except:
            product = None

        try:
            Review.objects.create(
                review_id  = review['review_id'],
                username   = user,
                product_id = product,

                date       = review['date'],
                rating     = review['rating'],
                content    = review['content'],
                location   = review['location']
            )
        
        except IntegrityError:
            pass

def main():
    # input_merchant()
    # input_product()
    # input_user()
    input_review()

if __name__ == '__main__':
    main()