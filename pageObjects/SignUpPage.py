from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class SignUpPage:
    def __init__(self, driver):
        self.driver = driver

    signup = (By.XPATH, "//button[contains(text(),'Sign up')]")
    email = (By.ID, "email")
    name = (By.ID, "first_name" )
    password = (By.ID, "password")
    address = (By.ID, "address")
    zipcode = (By.ID, "zip_code")
    phone = (By.ID, "phone")
    city = (By.ID, "city")
    submit = (By.XPATH, "//button[@type='submit']")

    def getCookie(self):
        #covid 19 popup closing implemented with explicitWait as it is a Modal Dialog Box
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='modal fade in show']//button[@class='close pull-right']")))

    def getSignup(self):
        #go to signup page
        return self.driver.find_element(*SignUpPage.signup)

    def getPopupclose(self):
        #popup closing
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn other-user']")))

    def getEmail(self):
        return self.driver.find_element(*SignUpPage.email)

    def getName(self):
        return self.driver.find_element(*SignUpPage.name)

    def getPassword(self):
        return self.driver.find_element(*SignUpPage.password)

    def getAddress(self):
        return self.driver.find_element(*SignUpPage.address)

    def getZipcode(self):
        return self.driver.find_element(*SignUpPage.zipcode)

    def getPhone(self):
        return self.driver.find_element(*SignUpPage.phone)

    def getCity(self):
        return self.driver.find_element(*SignUpPage.city)

    def getSubmit(self):
        return self.driver.find_element(*SignUpPage.submit)





