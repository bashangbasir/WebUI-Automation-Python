"""
This class contain Amazon main page object 
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class AmazonPage():
    
    WEBSITE_NAME = "Amazon.com"
    BASE_URL = "https://www.amazon.com/"
    SEARCH_TEXTBOX_LOCATOR = (By.ID,"twotabsearchtextbox")
    SEARCH_BUTTON_LOCATOR = (By.ID,"nav-search-submit-button")
    SEARCH_RESULT_DIV_LOCATOR = (By.XPATH,"*//div[@data-component-type='s-search-result']")
    PRODUCT_NAME = (By.XPATH,"*//a[@class='a-link-normal a-text-normal']/span[@class='a-size-medium a-color-base a-text-normal']")
    PRODUCT_PRICE_WHOLE = (By.XPATH,"*//span[@class='a-price-whole']")
    PRODUCT_PRICE_FRACTION = (By.XPATH,"*//span[@class='a-price-fraction']")
    PRODUCT_LINK = (By.XPATH,"*//a[@class='a-link-normal a-text-normal']")


    def __init__(self, driver):
        self.driver = driver


    def load_page(self):
        self.driver.get(self.BASE_URL)
        

    def search_item(self,item):
        self.driver.find_element(*self.SEARCH_TEXTBOX_LOCATOR).send_keys(item)
        self.driver.find_element(*self.SEARCH_BUTTON_LOCATOR).click()

    def get_searchresult(self):
        #get the list search result webelements
        search_results_elems = self.driver.find_elements(*self.SEARCH_RESULT_DIV_LOCATOR)
        validated_results = []
        #iterate in each web element to get product name, product price and product link 
        for result_elem in search_results_elems: 
            product_name = result.find_element(*self.PRODUCT_NAME).text
            
            #validate the product name is Iphone 11 related.
            if "iphone 11" not in product_name.lower():
                continue

            try :
                product_price = result.find_element(*self.PRODUCT_PRICE_WHOLE).text +"."+ result.find_element(*self.PRODUCT_PRICE_WHOLE).text
            except:
                product_price = None
            product_link = str(result.find_element(*self.PRODUCT_LINK).get_attribute("href"))
            
            validated_results.append([self.WEBSITE_NAME,product_name,product_price,product_link])
            
        return validated_results

