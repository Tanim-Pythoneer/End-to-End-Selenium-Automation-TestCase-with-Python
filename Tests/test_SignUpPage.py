import pytest

from TestData.SignupData import SignupData
from Utilities.BaseClass import BaseClass
from pageObjects.SignUpPage import SignUpPage


class TestSignUpPage(BaseClass):

    def test_signup(self, getData):
        log = self.getLogger()
        signupPage = SignUpPage(self.driver)

        signupPage.getCookie().click()
        signupPage.getSignup().click()
        signupPage.getPopupclose().click()
        signupPage.getEmail().send_keys(getData["Email"])
        signupPage.getName().send_keys(getData["Name"])
        signupPage.getPassword().send_keys(getData["Password"])
        signupPage.getAddress().send_keys(getData["Address"])
        log.warning("Address accepted with Numerical value only, for example 000 used in my case")
        signupPage.getZipcode().send_keys(getData["Postcode"])
        signupPage.getPhone().send_keys(getData["Phone"])
        log.warning("Phone number accepted with alphabetical value")
        signupPage.getCity().send_keys(getData["City"])
        signupPage.getSubmit().click()
        log.info("Signup process succeeded")

    @pytest.fixture(params=SignupData.test_signup_data)
    def getData(self, request):
        return request.param
