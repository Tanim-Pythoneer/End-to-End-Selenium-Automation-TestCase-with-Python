import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class LoggedOutRentPage:
    def __init__(self, driver):
        self.driver = driver

    lo_rentItem = (By.XPATH, "//h2[contains(text(),'Rent items')]")
    lo_productClick = (By.XPATH, "//app-product-thumbnail[2]//div[1]//div[2]//a[1]//div[1]")
    lo_addCartClick = (By.XPATH, "//button[@class='btn cartbtnpd']")
    lo_checkoutClick = (By.XPATH, "//button[@class='btn cartpagebtn mt-14']")



    def getlo_wait(self):
        return self.driver.implicitly_wait(10)

    def getpopup(self):
        #covid 19 popup closing implemented with explicitWait as it is a Modal Dialog Box
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='modal fade in show']//button[@class='close pull-right']")))

    def getlo_rentItem(self):
        return self.driver.find_element(*LoggedOutRentPage.lo_rentItem)

    def getlo_productClick(self):
        return self.driver.find_element(*LoggedOutRentPage.lo_productClick)

    def getlo_addCartclick(self):
        return self.driver.find_element(*LoggedOutRentPage.lo_addCartClick)

    def getlo_checkoutClick(self):
        return self.driver.find_element(*LoggedOutRentPage.lo_checkoutClick)



#driver.find_element_by_xpath("//h2[contains(text(),'Rent items')]").click()
#driver.find_element_by_xpath("//app-product-thumbnail[2]//div[1]//div[2]//a[1]//div[1]").click()
#driver.find_element_by_xpath("//button[@class='btn cartbtnpd']").click()
#driver.find_element_by_xpath("//button[@class='btn cartpagebtn mt-14']").click()

