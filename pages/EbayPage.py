"""
This class contain Ebay main page object 
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class EbayPage():
    
    WEBSITE_NAME = "eBay"
    URL = "https://www.ebay.com.my/"
    SEARCH_TEXTBOX_LOCATOR = (By.ID,"gh-ac")
    SEARCH_BUTTON_LOCATOR = (By.ID,"gh-btn")
    SEARCH_RESULT_LI_LOCATOR = (By.XPATH,"//li[@class='s-item    ']")
    PRODUCT_NAME = (By.XPATH,"*//h3[@class='s-item__title']")
    PRODUCT_PRICE = (By.XPATH,"//span[@class='s-item__price']")
    PRODUCT_LINK = (By.XPATH,"//a[@class='s-item__link']")

    def __init__(self, driver):
        self.driver = driver


    def load_page(self):
        self.driver.get(self.URL)
        

    def search_item(self,item):
        self.driver.find_element(*self.SEARCH_TEXTBOX_LOCATOR).send_keys(item)
        self.driver.find_element(*self.SEARCH_BUTTON_LOCATOR).click()

    def get_searchresult(self):
        search_result_elems = self.driver.find_elements(*self.SEARCH_RESULT_LI_LOCATOR)
        validated_results = []
        
        for result_elem in search_result_elems:
            product_name = result_elem.find_element(*self.PRODUCT_NAME).text
            
            if "iphone 11" not in product_name.lower():
                continue
            try:
                product_price = result_elem.find_element(*self.PRODUCT_PRICE)
            except:
                product_price = None
            product_link = result_elem.find_element(*self.PRODUCT_LINK).get_attribute("href")
            validated_results.append([self.WEBSITE_NAME,product_name,product_price,product_link])
        return validated_results
            






