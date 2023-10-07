from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import uuid
import time
import pandas as pd
import re

def save_to_csv(reviews):
    table = pd.DataFrame(reviews)
    table.to_csv("reviews.csv")

driver = webdriver.Chrome()

driver.get("https://shopee.sg/")

actions = ActionChains(driver)

searchbar = driver.find_element(By.CLASS_NAME, "shopee-searchbar-input__input")
searchbar.send_keys("Headphone")
searchbar.send_keys(Keys.RETURN)

# Wait till it locates the element; load the page
loginKey = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "loginKey"))
)
loginKey.send_keys("jeannie208")

# Locate the login password box, fill in, and then proceed to log in to the account
loginPassword = driver.find_element(By.NAME, "password")
loginPassword.send_keys("Jean060606")
loginPassword.send_keys(Keys.RETURN)

# ---------------------------------------------------------------------------------------------------
list_of_customerReviews = []
try:
    # Wait for the page to load
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.CLASS_NAME, "shopee-search-item-result__item"))
    )
    page = 1
    list_of_products = driver.find_elements(By.CLASS_NAME, "shopee-search-item-result__item")

    mainNextPage = True
    while mainNextPage:
        try:
            for num in range(len(list_of_products)):
                print("\npage {} --- {} product: start".format(page,num+1))
                # Wait for the list of product page to load
                WebDriverWait(driver, 60).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "shopee-search-item-result__item"))
                )

                # Locate the specific/next to-be-click product
                product = driver.find_elements(By.CLASS_NAME, "shopee-search-item-result__item")[num]

                # Actions to move to element and click
                actions.move_to_element(product).perform()
                actions.click(product).perform()

                print("\tclicked product")
                # Wait for the page to load
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "page-product"))
                )
                time.sleep(3)
                productName = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[1]/div/div[2]/section[1]/section[2]/div/div[1]/span")

                # Scroll down to load the rest of the contents of the page
                driver.execute_script("window.scrollTo(0, 1500)")

                # Check if there exist a review
                try:
                    print("\tchecking for review")
                    # Wait for the remaining contents to load
                    wait = WebDriverWait(driver, 10).until(
                       EC.presence_of_element_located((By.CLASS_NAME, "product-ratings"))
                    )
                    #time.sleep(3)
                    actions.move_to_element(wait).perform()

                    # Locate the reviews for the first round of loop only - if fail to locate the elements, means there are no reviews.
                    reviewsOnPage = driver.find_elements(By.CSS_SELECTOR, ".shopee-product-rating__main")

                    # Generate a unique ID
                    productID = uuid.uuid4()

                    nextPage = True
                    while nextPage:
                        # Allow 1 second to load the page
                        time.sleep(0.5)
                        customerReviews = {}

                        # Locate the elements
                        reviewsOnPage = driver.find_elements(By.CSS_SELECTOR, ".shopee-product-rating__main")
                        ratingsOnPage = driver.find_elements(By.CSS_SELECTOR, "div[class='shopee-product-rating__rating']")
                        usernameOnPage = driver.find_elements(By.CSS_SELECTOR, ".shopee-product-rating__author-name")
                        commentDateTimesOnPage = driver.find_elements(By.CSS_SELECTOR, ".shopee-product-rating__time")
                        nextButton = driver.find_element(By.CSS_SELECTOR, ".shopee-icon-button--right")

                        print("\tread", end=" |")
                        # Loop the 6 customer reviews - per page
                        for number in range(len(usernameOnPage)):

                            star = ratingsOnPage[number].find_elements(By.CSS_SELECTOR, ".icon-rating-solid--active")
                            dateTimeElementText = usernameOnPage[number].find_element(By.XPATH, "following-sibling::*[2]").text
                            dateTimePattern = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}"
                            dateTimeSearch = re.search(dateTimePattern, dateTimeElementText)

                            customerReviews["Product ID"] = str(productID)
                            customerReviews["Product Name"] = productName.text
                            customerReviews["Username"] = usernameOnPage[number].text
                            customerReviews["Rating"] = len(star)
                            customerReviews["DateTime"] = dateTimeSearch.group()

                            # Get reviews without comments
                            try:
                                # Get comment
                                review = reviewsOnPage[number].find_element(By.CSS_SELECTOR, "div[class='Rk6V+3']")

                                # Generate a unique ID
                                commentID = uuid.uuid4()

                                customerReviews["Comment ID"] = str(commentID)
                                customerReviews["Comments"] = review.text

                            except NoSuchElementException:
                                customerReviews["Comment ID"] = ""
                                customerReviews["Comments"] = ""


                            list_of_customerReviews.append(customerReviews.copy())

                        # Check if there is no pages left
                        lastPageButton = nextButton.find_element(By.XPATH, "preceding-sibling::*[1]")

                        # Actions to move to element
                        actions.move_to_element(lastPageButton).perform()

                        if "shopee-button-solid--primary" in lastPageButton.get_attribute("class"):
                            nextPage = False
                            break

                        actions.click(nextButton).perform()

                    print("\npage {} --- {} product: end".format(page,num+1))

                    save_to_csv(list_of_customerReviews)
                    print("saved to csv ")

                    # Return to list of products page
                    driver.back()

                # If there are no reviews found, then return back to list of products
                except NoSuchElementException:
                    driver.back()
                    print("\tno reviews")

                    save_to_csv(list_of_customerReviews)
                    print("saved to csv ")

                    pass

                except Exception:
                    driver.back()
                    print("\t Could be loading error")

                    save_to_csv(list_of_customerReviews)
                    print("saved to csv ")

                    pass
        except Exception:
            driver.back()
            print("prob error")
            pass

        print("check for main next button")
        mainNextButton = WebDriverWait(driver, 30).until(
                   EC.presence_of_element_located((By.CSS_SELECTOR, ".shopee-icon-button--right")))
        print("done - check for main next button")

        # Check if there is no main pages left
        lastPageButton = mainNextButton.find_element(By.XPATH, "preceding-sibling::*[1]")

        # Actions to move to element
        actions.move_to_element(lastPageButton).perform()

        if "shopee-button-solid--primary" in lastPageButton.get_attribute("class"):
            mainNextPage = False
            print("end of main page")
            break

        actions.click(mainNextButton).perform()

        print("clicked main next button")
        page += 1

    save_to_csv(list_of_customerReviews)
    print("saved to csv ")

except Exception:
    driver.refresh()
    pass



