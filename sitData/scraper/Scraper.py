# ==================== #
# ===== PACKAGES ===== #
# ==================== #
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup

import pandas as pd
import time

import uuid

import os

# ========================== #
# ===== INITIALISATION 1 ===== #
# ========================== #
#chromedriver_path = os.path.expanduser("~/GitLocal/SitShop/sitData/scraper/chromedriver_v117.exe")
#s = Service(chromedriver_path)
#driver = webdriver.Chrome(service = s)
driver = webdriver.Chrome()
driver.get("https://shopee.sg/")

# ============================ #
# ===== INITIALISATION 2 ===== #
# ============================ #
time.sleep(2)
search_bar = driver.find_element(By.CLASS_NAME, "shopee-searchbar-input__input")
search_bar.send_keys("headphone")
search_bar.send_keys(Keys.RETURN)

time.sleep(1)
username_bar = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.NAME, "loginKey"))
)
username_bar.send_keys("newsswen")

time.sleep(1)
password_bar = driver.find_element(By.NAME, "password")
password_bar.send_keys("123NEWSabcSWEN")

time.sleep(1)
password_bar.send_keys(Keys.RETURN)

# ===================== #
# ===== SCRAPING  ===== #
# ===================== #

merchant_output = []
product_output  = []
review_output   = []

product_page    = 0
# 1st while loop to loop through all product pages
while True:
    product_page += 1
    product_counter = 0
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.CLASS_NAME, "shopee-search-item-result__item"))
    )
    product_list = driver.find_elements(By.CLASS_NAME, "shopee-search-item-result__item")

    # Sanity check 1 : Product List Page
    print(f"{len(product_list)} products on product page {product_page}!")

    for product in product_list:
        time.sleep(2)
        #product_counter += 1
        product = driver.find_elements(By.CLASS_NAME, "shopee-search-item-result__item")[product_counter]
        time.sleep(5)
        product.click()

        time.sleep(2)
        page_source = driver.page_source
        soup = BeautifulSoup(page_source)

        # Sanity check 2 : Product Page
        print(f"Scraping Merchant and Product Info of Product_{product_counter}")

        # ==================== #
        # ===== MERCHANT ===== #
        # ==================== #
        merchant_obj = {}

        merchant_id = str(uuid.uuid4())

        merchant_obj["merchant_id"] = merchant_id
        merchant_obj["name"]        = soup.find("div", class_="VlDReK").text

        merchant_info = soup.find("div", class_="Po6c6I")
        merchant_info = merchant_info.find_all(class_="R7Q8ES")

        for info in merchant_info:
            label = info.find("label").text
            span  = info.find("span").text
            merchant_obj[label] = span

        merchant_output.append(merchant_obj)

        # =================== #
        # ===== PRODUCT ===== #
        # =================== #
        product_obj = {}

        product_id = str(uuid.uuid4())

        product_obj["product_id"]  = product_id
        product_obj["merchant_id"] = merchant_id

        product_info = soup.find("section", class_="RBf1cu")

        # Name, Preferred and Mall
        name_section = product_info.find("div", class_="_44qnta")
        product_obj["name"] = name_section.find("span").text

        try:
            name_section.find("svg")
            product_obj["preferred"] = 0
            product_obj["mall"]      = 1
        except:
            product_obj["preferred"] = 0
            product_obj["mall"]      = 0

        try:
            name_section.find("div")
            product_obj["preferred"] = 1
            product_obj["mall"]      = 0
        except:
            product_obj["preferred"] = 0
            product_obj["mall"]      = 0

        # Ratings
        rating_section = product_info.find("div", class_="X5u-5c")
        try:
            rating = rating_section.find_all("div", class_="_1k47d8")
            product_obj["avg_rating"]   = rating[0].text
            product_obj["total_rating"] = rating[-1].text
        except:
            product_obj["avg_rating"]   = None
            product_obj["total_rating"] = None

        try:
            product_obj["total_sold"]  = rating_section.find("div", class_="e9sAa2").text
        except:
            product_obj["total_sold"]  = 0
        # Other info
        product_obj["price"] = product_info.find("div", class_="pqTWkA").text
        product_obj["qty_avail"] = product_info.find("section", class_="flex items-center _6lioXX").find_all("div")[-1].text
        try:
            product_obj["fav_count"]   = soup.select_one(".flex.items-center._3jkKrB .Ne7dEf").text
        except:
            product_obj["fav_count"]   = 0

        # Description
        try:
            desc_section = soup.find("div", class_='f7AU53')
            sentence_list = desc_section.find_all('p')
            sentence_list = [sentence.text for sentence in sentence_list]
            product_obj['description'] = ' '.join(sentence_list)
        except:
            product_obj['description'] = None

        # Product image src
        try:
            product_obj["img_src"] = soup.find("div", class_="LsMpPX").find("img")['src']
        except:
            product_obj["img_src"] = soup.find("div", class_="LmLCVP").find("picture").find("img")['src']

        product_output.append(product_obj)

        # =================== #
        # ===== REVIEW ====== #
        # =================== #
        review_page = 0
        while True:
            time.sleep(1)
            review_page += 1
            review_list = driver.find_elements(By.CLASS_NAME, "shopee-product-rating")

            if len(review_list) > 0:
                # Sanity check 3 : Product List Page
                (f"{len(review_list)} reviews for product_{product_counter}_reviewpage_{review_page}!")

                for review in review_list:
                    review_obj =  {}
                    review_obj["review_id"]   = str(uuid.uuid4())
                    review_obj["username"]    = review.find_element(By.CSS_SELECTOR, ".shopee-product-rating__author-name").text
                    review_obj["merchant_id"] = merchant_id
                    review_obj["product_id"]  = product_id

                    review_obj["date"]        = review.find_element(By.CSS_SELECTOR, "div[class='shopee-product-rating__time']").text.split(" | ")[0]
                    review_obj["rating"]      = len(review.find_elements(By.CSS_SELECTOR, ".icon-rating-solid--active"))

                    try:
                        review_obj["content"] = review.find_element(By.CSS_SELECTOR, "div[class='Rk6V+3']").text
                    except:
                        review_obj["content"] = None

                    review_output.append(review_obj)

                review_page_controller   = driver.find_element(By.CLASS_NAME, "shopee-page-controller")
                review_page_list         = review_page_controller.find_elements(By.CSS_SELECTOR, "button")
                last_page_display        = review_page_list[-2].text
                next_page_button         = review_page_list[-1]

                if last_page_display == '...':
                    next_page_button.click()

                elif int(last_page_display) > review_page:
                    next_page_button.click()

                else:
                    driver.back()
                    product_counter += 1

                    merchant_table = pd.DataFrame(merchant_output)
                    product_table = pd.DataFrame(product_output)
                    review_table = pd.DataFrame(review_output)

                    merchant_table.to_csv("newMerchant.csv", index=False)
                    product_table.to_csv("newProduct.csv", index=False)
                    review_table.to_csv("newReview.csv", index=False)
                    break
            else:
                driver.back()
                product_counter += 1

                merchant_table = pd.DataFrame(merchant_output)
                product_table = pd.DataFrame(product_output)
                #review_table = pd.DataFrame(review_output)

                merchant_table.to_csv("newMerchant.csv", index=False)
                product_table.to_csv("newProduct.csv", index=False)
                #review_table.to_csv("newReview.csv", index=False)
                break

    product_page_controller   = driver.find_element(By.CLASS_NAME, "shopee-page-controller")
    product_page_list         = product_page_list.find_elements(By.CSS_SELECTOR, "button")
    last_page_display         = product_page_list[-2].text
    next_page_button          = product_page_list[-1]

    if last_page_display == '...':
        next_page_button.click()

    elif int(last_page_display) > product_page:
        next_page_button.click()

    else:
        break            

# ======================== #
# ===== OUTPUT FILE  ===== #
# ======================== #
merchant_table = pd.DataFrame(merchant_output)
product_table  = pd.DataFrame(product_output)
review_table   = pd.DataFrame(review_output)

merchant_table.to_csv("newMerchant.csv", index=False)
product_table.to_csv("newProduct.csv", index=False)
review_table.to_csv("newReview.csv", index=False)