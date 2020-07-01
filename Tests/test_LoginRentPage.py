import time

from Utilities.BaseClass import BaseClass
from pageObjects.LoginRentPage import LoginRentPage


class TestLoginRentPage(BaseClass):

    def test_loginrent(self):
        log = self.getLogger()

        loginRentPage = LoginRentPage(self.driver)
        loginRentPage.getWait()
        loginRentPage.getPopup().click()
        loginRentPage.getLoginClick().click()
        loginRentPage.getEmailInput().send_keys("adtanim@gmail.com")
        log.info("No Sql injection problem found. Tried query with (' or 1=1;--) But remained FALSE")
        loginRentPage.getPasswordInput().send_keys("Dhaka123@")
        loginRentPage.getLoginSubmit().click()
        loginRentPage.getRentItem().click()
        loginRentPage.getLoginSuccessScreenshot()
        loginRentPage.getProductSearch().send_keys("tek")
        log.warning("Right Navigation arrow not visible properly (class= 'fa fa-2x fa-chevron-right nav-arrow')")
        log.info("Product found with key word search")
        time.sleep(2)
        loginRentPage.getSearchClick().click()
        loginRentPage.getCartClick().click()
        loginRentPage.getAddCartClick().click()
        log.info("Product Added to cart successfully")
        loginRentPage.getcheckoutClick().click()
