from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup
import requests

import pandas as pd
import time
import os

DIR = f'asset/2023/10/03/'
FILENAME = f'data_03.csv'
os.makedirs(DIR, exist_ok=True)

s = Service("C:/Users/edmund/GitLocal/SitShop/PythonData/chromedriver.exe")
driver = webdriver.Chrome(service = s)

def review_scraper(username, driver=driver):
    driver.get(f"https://www.carousell.sg/u/{username}/reviews/")

    while True:
        try:
            load_more_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[1]/div[1]/div[3]/div[2]/div/button")
            load_more_button.click()
            time.sleep(1)
        except:
            break

    customer_cards = driver.find_elements(By.CSS_SELECTOR, "li[class^='D_WK']")
    
    customer_list = []

    counter = 0 
    for customer in customer_cards:
        if counter == 0:
            print("scraping starts!")
        elif counter%50 == 0:
            print(f"scraped {counter} customers!")
        
        customer_dict = {}
    
        customer_dict['reviewee'] = username
        
        top = customer.find_element(By.CSS_SELECTOR, "div[class^='D_OH']")
        
        reviewer = top.find_elements(By.CSS_SELECTOR, "span")[0]
        reviewer = reviewer.text
        customer_dict['reviewer'] = reviewer
        
        identity = top.find_elements(By.CSS_SELECTOR, "span")[1]
        identity = identity.text.split(" ")[-1]
        customer_dict['reviewer_identity'] = identity
    
        date = top.find_elements(By.CSS_SELECTOR, "span")[2]
        date = date.text
        customer_dict['review_date'] = date
    
        star = customer.find_element(By.CSS_SELECTOR, "div[class^='D_Hj']")
        star = star.get_attribute('aria-label').split(" ")[0]
        star = float(star)
        customer_dict['review_star'] = star
    
        try:
            tag_list = customer.find_element(By.CSS_SELECTOR, "div[class^='D_OR']")
            tag_list = tag_list.find_elements(By.CSS_SELECTOR, "div[class^='D_OS']")
            for tag in tag_list:
                tag = tag.text
                customer_dict[tag] = 1
                
        except:
            pass
    
        review = customer.find_element(By.CSS_SELECTOR, "p[data-testid='feedback-review']")
        review = review.text
        customer_dict["review"] = review
    
        customer_list.append(customer_dict)
        counter += 1

    return customer_list

def save_csv(dataframe):
    with open(DIR + FILENAME, 'wb') as file:
        dataframe.to_csv(file)

data_row = 0

while data_row < 100000:
    if data_row == 0:
        customer_list = review_scraper('jeankini')
        customer_df = pd.DataFrame(customer_list)
        customer_df = customer_df.fillna(0)
        
        data_row = len(customer_df)
        print(data_row)
        save_csv(customer_df)
        
        
    else:
        for seller in customer_df[customer_df['reviewer_identity'] == 'seller']['reviewer']:
            if seller not in set(customer_df['reviewee']):
                new_customer_list = review_scraper(seller)
                customer_list = customer_list + new_customer_list
                customer_df = pd.DataFrame(customer_list)
                customer_df = customer_df.fillna(0)

                data_row = len(customer_df)
                print(data_row)
                save_csv(customer_df)

