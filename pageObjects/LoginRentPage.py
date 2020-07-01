import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class LoginRentPage:
    def __init__(self, driver):
        self.driver = driver

    login = (By.XPATH, "//button[@class='btn loginbtn']")
    email = (By.ID,"email")
    password = (By.XPATH, "//input[@id='password']")
    loginSubmit = (By.XPATH, "//button[@class='btn btn-default btn-login btn-lg']")
    rentItem = (By.XPATH, "//h2[contains(text(),'Rent items')]")
    productSearch = (By.XPATH, "//div[@id='adv-search']//input[@id='search-box']")
    searchClick = (By.XPATH, "//button[@class='btn filterbtn ml-3']")
    cartClick = (By.XPATH, "//div[@class='cartbtn']")
    addCartClick = (By.XPATH, "//button[@class='btn cartbtnpd']")
    checkoutClick = (By.XPATH, "//button[@class='btn cartpagebtn mt-14']")



    def getWait(self):
        return self.driver.implicitly_wait(10)

    def getPopup(self):
        #covid 19 popup closing implemented with explicitWait as it is a Modal Dialog Box
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='modal fade in show']//button[@class='close pull-right']")))

    def getLoginClick(self):
        return self.driver.find_element(*LoginRentPage.login)

    def getEmailInput(self):
        return self.driver.find_element(*LoginRentPage.email)

    def getPasswordInput(self):
        return self.driver.find_element(*LoginRentPage.password)

    def getLoginSubmit(self):
        return self.driver.find_element(*LoginRentPage.loginSubmit)

    def getRentItem(self):
        return self.driver.find_element(*LoginRentPage.rentItem)

    def getLoginSuccessScreenshot(self):
        return self.driver.get_screenshot_as_file("loginsuccess.png")

    def getProductSearch(self):
        return self.driver.find_element(*LoginRentPage.productSearch)

    time.sleep(2)

    def getSearchClick(self):
        return self.driver.find_element(*LoginRentPage.searchClick)

    def getCartClick(self):
        return self.driver.find_element(*LoginRentPage.cartClick)

    def getAddCartClick(self):
        return self.driver.find_element(*LoginRentPage.addCartClick)

    def getcheckoutClick(self):
        return self.driver.find_element(*LoginRentPage.checkoutClick)



#driver.find_element_by_xpath("//button[@class='btn loginbtn']").click()
#driver.find_element_by_id("email").send_keys("adtanim@gmail.com")
#driver.find_element_by_xpath("//input[@id='password']").send_keys("Dhaka123@")
#driver.find_element_by_xpath("//button[@class='btn btn-default btn-login btn-lg']").click()

#rent item as logged in user
#driver.find_element_by_xpath("//h2[contains(text(),'Rent items')]").click()
#driver.get_screenshot_as_file("loginsuccess.png")
#driver.find_element_by_xpath("//div[@id='adv-search']//input[@id='search-box']").send_keys("tek")
time.sleep(2)
#driver.find_element_by_xpath("//button[@class='btn filterbtn ml-3']").click()
#driver.find_element_by_xpath("//div[@class='cartbtn']").click()
#right nav arrow for slideshow is not visible
#driver.find_element_by_xpath("//button[@class='btn cartbtnpd']").click()
#product added to cart
#driver.find_element_by_xpath("//button[@class='btn cartpagebtn mt-14']").click()
#checkout successful