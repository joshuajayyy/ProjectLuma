import time

from pages.header_links import HeaderLinks
from pages.home_page import HomePage
from pages.login_page import LoginPage
from testData.input_data import InputData
from utilities.base_class import BaseClass


class TestHoverProduct(BaseClass):

    def test_hover_product(self):
        header_link = HeaderLinks(self.driver)
        login = LoginPage(self.driver)
        home = HomePage(self.driver)

        header_link.clickLoginButton().click()

        login.setEmail().send_keys(InputData().getUserEmail())
        login.setPassword().send_keys(InputData().getUserPassword())
        login.clickSubmit().click()

        self.execute_scroll_view(home.scroll)
