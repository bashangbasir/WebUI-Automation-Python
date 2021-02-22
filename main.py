
from pages.AmazonPage import AmazonPage
from pages.EbayPage import EbayPage
from selenium import webdriver 

def setup (browser):
    if browser.lower() == "chrome":
        driver = webdriver.Chrome("./resources/chromedriver.exe")
    elif browser.lower() == "firefox":
        driver = webdriver.Firefox(executable_path="./resources/geckodriver.exe")
    else:
        raise Exception("{} Browser is not supported".format(browser))

    #Implicit wait 
    driver.implicitly_wait(3)
    return driver  

def teardown(driver):
    driver.quit()

if __name__ == "__main__":
    
    driver = setup("firefox")
    
    amazon_page = AmazonPage(driver)
    amazon_page.load_page()
    amazon_page.search_item("iPhone 11")
    #get the list of the result that have been verified is iphone11 related
    amazon_results = amazon_page.get_searchresult()

    ebay_page = EbayPage(driver)
    ebay_page.load_page()
    ebay_page.search_item("iPhone 11")
    #get the list of the result that have been verified is iphone11 related
    ebay_results = ebay_page.get_searchresult()
    

    
    #teardown(driver)

