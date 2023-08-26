import pytest

from pages.header_links import HeaderLinks
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.whatsnew_page import WhatsNewPage
from testData.input_data import InputData
from utilities.base_class import BaseClass


class TestProcessAnOrder(BaseClass):

    @pytest.mark.usefixtures("getData", "getProductInfo")
    def test_processAnOrder(self, getData, getProductInfo):
        log = self.getlogger()
        signIn = LoginPage(self.driver)
        signIn.clickLoginButton().click()

        signIn.setEmail().send_keys(InputData().getUserEmail())
        signIn.setPassword().send_keys(getData["password"])
        signIn.clickLoginButton().click()

        headerLink = HeaderLinks(self.driver)
        headerLink.clickWhatsNew().click()

        self.explicitWait(WhatsNewPage.target_element)
        whats_new = WhatsNewPage(self.driver)
        whats_new.productSearch(getProductInfo["product_name"])

        product_page = ProductPage(self.driver)

        product_page.setSize(getProductInfo["size"])
        product_page.setColor().click()
        product_page.setQuantity().send_keys(getProductInfo["quantity"])
        product_page.clickAddToCart().click()

        """
        log.info("Customer {}, {} ordered {} item/s of {} size {} with an SKU of {}".format(
            getData["lastname"], getData["firstname"], getProductInfo["quantity"], getProductInfo["size"],
            getProductInfo["product_name"], product_page.getSKU()))
        """

        self.explicitWait(headerLink.wait)
        headerLink.cartIcon().click()

        self.explicitWait(headerLink.wait2)
        headerLink.proceedToCheckOut().click()
