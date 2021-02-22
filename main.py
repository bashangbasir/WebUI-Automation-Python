
from pages.AmazonPage import AmazonPage
from pages.EbayPage import EbayPage
from selenium import webdriver 

def setup (browser):
    if browser.lower() == "chrome":
        driver = webdriver.Chrome("./resources/chromedriver.exe")
    elif browser.lower() == "firefox":
        driver = webdriver.Firefox()
    else:
        raise Exception("{} Browser is not supported".format(browser))

    #Implicit wait 
    driver.implicitly_wait(3)

    return driver  

def teardown(driver):
    driver.quit()
    

if __name__ == "__main__":
    
    driver = setup("Chrome")
    amazon_page = AmazonPage(driver)
    amazon_page.load_page()
    amazon_page.search_item("iPhone 11")
    amazon_page.get_searchresult_webelements()
    

    # ebay_page = EbayPage(driver)
    # ebay_page.load_page()
    # ebay_page.search_item("iPhone 11")
    
    teardown(driver)

