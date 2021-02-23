
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
    #driver.maximize_windows()
    return driver  

def teardown(driver):
    driver.quit()

def sort_combined_result(results):
    results.sort(key=getPrice)
    return results

def getPrice(list_content):
    #return price 
    return list_content[2]


if __name__ == "__main__":
    
    driver = setup("chrome")
    
    amazon_page = AmazonPage(driver)
    amazon_page.load_page()
    #need to change currency to MYR since amazon price in USD. 
    amazon_page.change_currency_to_myr()
    amazon_page.search_item("iPhone 11")
    #get the list of the result that have been verified is iphone11 related
    amazon_results = amazon_page.get_searchresult()

    ebay_page = EbayPage(driver)
    ebay_page.load_page()
    ebay_page.search_item("iPhone 11")
    #get the list of the result that have been verified is iphone11 related
    ebay_results = ebay_page.get_searchresult()
    
    all_results = amazon_results + ebay_results
    sorted_results = sort_combined_result(all_results)
    #use for debugging - see the price is sorted ascending order
    for item in sorted_results:
        print(item[2])
    for item in sorted_results:
        print(item)
    
    teardown(driver)

