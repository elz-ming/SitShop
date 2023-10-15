import os
import sys
import django
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sitProject.settings')
django.setup()

import time

import pandas as pd
from sitApp.models import Merchant, Product, User, Review
from django.db import IntegrityError

def input_merchant():
    start_time = time.time()

    merchant_df = pd.read_csv("./sitData/asset/etlMerchant.csv")
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
    
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Finish Inputting Merchant Data in {execution_time} seconds!")


def input_product():
    start_time = time.time()

    product_df  = pd.read_csv("./sitData/asset/etlProduct.csv")
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
    
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Finish Inputting Product Data in {execution_time} seconds!")


def input_user():
    start_time = time.time()

    user_df     = pd.read_csv("./sitData/asset/etlUser.csv")
    for index, user in user_df.iterrows():
        try:
            User.objects.create(
                username     = user['username'],
                no_review    = user['no_review'],
                review_list  = user['review_list'],
                no_product   = user['no_product'],
                product_dict = user['product_dict'],
                mean_rating  = user['mean_rating']
            )
        
        except IntegrityError:
            pass
    
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Finish Inputting User Data in {execution_time} seconds!")


def input_review():
    start_time = time.time()

    review_df   = pd.read_csv("./sitData/asset/etlReview.csv")
    counter = 0
    for index, review in review_df.iterrows():
        user    = User.objects.get(username=review['username'])
        product = Product.objects.get(product_id=review['product_id'])

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

        counter += 1
        if counter%1000 == 0:
            print(f"Inputted {counter} rows of data.")

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Finish Inputting Review Data in {execution_time} seconds!")


def update_product():
    start_time = time.time()

    product_df  = pd.read_csv("./sitData/asset/etlProduct.csv")
    for index, product in product_df.iterrows():
        try:
            p = Product.objects.get(product_id=product['product_id'])
            p.img_src = product['img_src']
            p.save()
        except IntegrityError:
            pass

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Finish Updating Product Data in {execution_time} seconds!")


def add_product():
    start_time = time.time()

    addProduct_df = pd.read_csv("./sitData/asset/addProduct.csv")
    for index, product in addProduct_df.iterrows():
        try:
            p = Product.objects.get(product_id=product['product_id'])
            p.avg_norm_rating   = product['avg_norm_rating']
            p.count_norm_rating = product['count_norm_rating']
            p.merchant_class    = product['merchant_class']
            p.credibility_score = product['credibility_score']
            p.pos_1             = product['pos_1']
            p.pos_2             = product['pos_2']
            p.pos_3             = product['pos_3']    
            p.neg_1             = product['neg_1']
            p.neg_2             = product['neg_2']
            p.neg_3             = product['neg_3']
            p.save()
        except IntegrityError:
            pass

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Finish Adding Product Data in {execution_time} seconds!")


def add_user():
    start_time = time.time()

    addUser_df    = pd.read_csv("./sitData/asset/addUser.csv")
    for index, user in addUser_df.iterrows():
        try:
            u = User.objects.get(username=user['username'])
            u.min_dist_username = user['min_dist_username']
            u.save()
        except IntegrityError:
            pass

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Finish Adding User Data in {execution_time} seconds!")


def main():
    # input_merchant()
    # input_product()
    # input_user()
    # input_review()
    # update_product()
    # add_product()
    add_user()

if __name__ == '__main__':
    main()