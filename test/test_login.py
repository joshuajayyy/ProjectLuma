import pytest

from pages.account_page import AccountPage
from pages.header_links import HeaderLinks
from pages.login_page import LoginPage
from testData.input_data import InputData
from utilities.base_class import BaseClass


class TestLoginPage(BaseClass):

    @pytest.mark.usefixtures("getData")
    @pytest.mark.successful_login
    def test_successful_login(self, getData):
        log = self.getlogger()
        log_in = LoginPage(self.driver)
        header_link = HeaderLinks(self.driver)

        header_link.clickLoginButton().click()
        log_in.setEmail().send_keys(InputData().getUserEmail())
        log_in.setPassword().send_keys(InputData().getUserPassword())
        log.info("User " + getData["firstname"] + " " + getData["lastname"] + " entered an email: " + InputData().getUserEmail())
        log_in.clickSubmit().click()

        current_url = self.driver.current_url
        assert current_url == "https://magento.softwaretestingboard.com/"