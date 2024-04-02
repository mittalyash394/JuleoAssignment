# from os import wait
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.amazon.in/")

class AddingItemsToCart():
    def locate_by_id_demo(self):
        driver.find_element("id", "twotabsearchtextbox").send_keys('iphone')
        driver.find_element("id", "nav-search-submit-button").click()
        # 1st element
        eles = driver.find_element("xpath", '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/span/div/div/div/div[1]/div/div[2]/div/span/a/div/img')
        eles.click()
        
        tabs = driver.window_handles
        driver.switch_to.window(tabs[1])
        count = 0
        # while count < 5:
        driver.execute_script("window.scrollTo(0, window.scrollY + 500);")
        # driver.implicitly_wait(5)
        element = driver.find_element("id", "buy-now-button")
        print(element.get_attribute("value"))
        element.click()
        time.sleep(5)
        
class UpdateAddressInformation():
    def updateAddress(self):
        time.sleep(2)
        driver.back()
        driver.find_element("id", "nav-global-location-popover-link").click()
        driver.find_element("id", "GLUXZipUpdateInput")
        driver.find_element("class", "a-button-input").click()
        time.sleep(5)


find_by_id = AddingItemsToCart()
find_by_id.locate_by_id_demo()

updateAddress = UpdateAddressInformation()
updateAddress.updateAddress()