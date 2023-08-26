import pytest

from pages.header_links import HeaderLinks
from pages.login_page import LoginPage
from testData.input_data import InputData
from utilities.base_class import BaseClass





class TestLoginPage(BaseClass):

    @pytest.mark.usefixtures("getData")
    def test_login(self, getData):
        log = self.getlogger()
        log_in = LoginPage(self.driver)
        header_link = HeaderLinks(self.driver)

        header_link.clickLoginButton().click()
        log_in.setEmail().send_keys(InputData().getUserEmail())
        log_in.setPassword().send_keys(getData["password"])
        log.info("User " + getData["firstname"] + " " + getData["lastname"] + " entered an email: " + InputData().getUserEmail())
        log_in.clickSubmit().click()
