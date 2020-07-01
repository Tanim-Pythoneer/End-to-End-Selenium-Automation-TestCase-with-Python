from Utilities.BaseClass import BaseClass
from pageObjects.loggedOutRentpage import LoggedOutRentPage


class TestLoggedoutRentPage(BaseClass):

    def test_loggedOutRentPage(self):
        log = self.getLogger()

        loggedoutRentPage = LoggedOutRentPage(self.driver)
        log.warning("'About', 'How Liiteri works' and 'Contact us' page opens in new window always. 'Subscription' page works normally.")
        loggedoutRentPage.getlo_wait()
        loggedoutRentPage.getpopup().click()
        loggedoutRentPage.getlo_rentItem().click()
        loggedoutRentPage.getlo_productClick().click()
        loggedoutRentPage.getlo_addCartclick().click()
        loggedoutRentPage.getlo_checkoutClick().click()
        log.info("User without loggin in can browse the product and add to cart but registration needed to checkout!")