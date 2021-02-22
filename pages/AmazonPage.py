"""
This class contain Amazon main page object 
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class AmazonPage():
    
    URL = "https://www.amazon.com/"
    SEARCH_TEXTBOX_LOCATOR = (By.ID,"twotabsearchtextbox")
    SEARCH_BUTTON_LOCATOR = (By.ID,"nav-search-submit-button")
    SEARCH_RESULT_DIV_LOCATOR = (By.XPATH,"*//div[@data-component-type='s-search-result']")
    PRODUCT_NAME = (By.XPATH,"*//a[@class='a-link-normal a-text-normal']/span[@class='a-size-medium a-color-base a-text-normal']")
    PRODUCT_PRICE_WHOLE = (By.XPATH,"*//span[@class='a-price-whole']")
    PRODUCT_PRICE_FRACTION = (By.XPATH,"*//span[@class='a-price-fraction']")


    def __init__(self, driver):
        self.driver = driver


    def load_page(self):
        self.driver.get(self.URL)
        

    def search_item(self,item):
        self.driver.find_element(*self.SEARCH_TEXTBOX_LOCATOR).send_keys(item)
        self.driver.find_element(*self.SEARCH_BUTTON_LOCATOR).click()

    def get_searchresult_webelements(self):
        #get the list search result webelements
        search_results = self.driver.find_elements(*self.SEARCH_RESULT_DIV_LOCATOR)
        #iterate in each web element to check the result is correct iphone 11 
        i =1
        for result in search_results: 
            product_name = result.find_element(*self.PRODUCT_NAME).text
            try :
                product_price = result.find_element(*self.PRODUCT_PRICE_WHOLE).text +"."+ result.find_element(*self.PRODUCT_PRICE_WHOLE).text
            except:
                product_price = None

            print (i,product_name,product_price)
            i += 1 


