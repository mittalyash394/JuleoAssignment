# from os import wait
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome() #to initializa the chrome driver
driver.maximize_window() #To maximize the window.
driver.get("https://www.amazon.in/") #The URL of the website that we want to automate


#Class to add the items in cart
class AddingItemsToCart():
    def locate_by_id_demo(self):
        #find element for search bar
        driver.find_element("id", "twotabsearchtextbox").send_keys('iphone')
        #find element for enter button search and click it.
        driver.find_element("id", "nav-search-submit-button").click()
        # 1st element
        #now, click on the first response after searching
        eles = driver.find_element("xpath", '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/span/div/div/div/div[1]/div/div[2]/div/span/a/div/img')
        eles.click()
        
        #A new tab is opened, go to new tab that opened by using driver.switch_to.window
        tabs = driver.window_handles
        driver.switch_to.window(tabs[1])
        driver.execute_script("window.scrollTo(0, window.scrollY + 500);")
        #since, the add to cart button was not working in selenium, tried to do with buy now button. and opened the login via gmail button.
        element = driver.find_element("id", "buy-now-button")
        print(element.get_attribute("value"))
        #Now, click on the buy now button for login
        element.click()
        time.sleep(5)
        
        
#for updating the address, a new method is invoked
class UpdateAddressInformation():
    def updateAddress(self):
        # time.sleep(2)
        #now, the driver will move backwards the gmail login screen.
        driver.back()
        #now, find the element for changing the Address
        driver.find_element("id", "nav-global-location-popover-link").click()
        print("YAHS")
        time.sleep(5)
        driver.find_element("id", "GLUXZipUpdateInput").send_keys('201301')
        print("mittal")
        # driver.find_element("xpath", '/html/body/div[14]/div/div/div/div/div[2]/div[3]/div[2]/div/div[2]/span/span/input').click()
        button = driver.find_element("xpath", '//*[@id="GLUXZipUpdate-announce"]')
        print(button.get_attribute("id"))
        time.sleep(10)
        button.click()
        # button.click()
        time.sleep(5)


find_by_id = AddingItemsToCart()
find_by_id.locate_by_id_demo()

updateAddress = UpdateAddressInformation()
updateAddress.updateAddress()