import time

from pages.header_links import HeaderLinks
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.product_hover import ProductHover
from testData.input_data import InputData
from utilities.base_class import BaseClass


class TestHoverProduct(BaseClass):

    def test_hover_product(self):
        header_link = HeaderLinks(self.driver)
        login = LoginPage(self.driver)
        home = HomePage(self.driver)
        hover = ProductHover(self.driver)

        header_link.clickLoginButton().click()

        login.setEmail().send_keys(InputData().getUserEmail())
        login.setPassword().send_keys(InputData().getUserPassword())
        login.clickSubmit().click()

        self.execute_scroll_view(home.scroll)
        hover.set_size_on_hover()
        hover.set_color_on_hover()
        hover.hover_element()
        hover.add_to_cart_on_hover().click()

        header_link.cartIcon().click()
        product_name = hover.get_product_hover_name()
        print(product_name)
