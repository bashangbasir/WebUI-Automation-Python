"""
This class contain Ebay main page object 
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class EbayPage():
    
    URL = "https://www.ebay.com.my/"
    SEARCH_TEXTBOX_LOCATOR = (By.ID,"gh-ac")
    SEARCH_BUTTON_LOCATOR = (By.ID,"gh-btn")

    def __init__(self, driver):
        self.driver = driver


    def load_page(self):
        self.driver.get(self.URL)
        

    def search_item(self,item):
        self.driver.find_element(*self.SEARCH_TEXTBOX_LOCATOR).send_keys(item)
        self.driver.find_element(*self.SEARCH_BUTTON_LOCATOR).click()

