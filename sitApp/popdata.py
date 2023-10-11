import pandas as pd
from models import Merchant
from django.db import IntegrityError

merchant_df = pd.read_csv("./sitData/asset/etlMerchant.csv")
product_df  = pd.read_csv("./sitData/asset/etlProduct.csv")
review_df   = pd.read_csv("./sitData/asset/etlReview.csv")
user_df     = pd.read_csv("./sitData/asset/etlUser.csv")

def main():
    for merchant in merchant_df:
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

if __name__ == '__main__':
    main()