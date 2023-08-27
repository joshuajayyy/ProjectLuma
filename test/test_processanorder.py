import pytest

from pages.check_out_page import CheckOutPage
from pages.header_links import HeaderLinks
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.whatsnew_page import WhatsNewPage
from testData.input_data import InputData
from utilities.base_class import BaseClass


class TestProcessAnOrder(BaseClass):

    @pytest.mark.usefixtures("getData", "getProductInfo", "getAddress", "getStates")
    def test_processAnOrder(self, getData, getProductInfo, getAddress, getStates):
        log = self.getlogger()
        header_link = HeaderLinks(self.driver)
        sign_in = LoginPage(self.driver)
        whats_new = WhatsNewPage(self.driver)
        product_page = ProductPage(self.driver)
        check_out_page = CheckOutPage(self.driver, getStates)

        # User Sign In
        header_link.clickLoginButton().click()

        # Enter username and password
        sign_in.setEmail().send_keys(InputData().getUserEmail())
        sign_in.setPassword().send_keys(InputData().getUserPassword())
        sign_in.clickSubmit().click()

        # Click on whats new page
        header_link.clickWhatsNew().click()

        # Navigate to whats new page and add product
        self.explicitWait(WhatsNewPage.target_element)
        whats_new.productSearch(getProductInfo["product_name"])

        # Set all necessary information from product page

        product_page.setSize(getProductInfo["size"])
        product_page.setColor().click()
        product_page.setQuantity().send_keys(getProductInfo["quantity"])
        product_page.clickAddToCart().click()

        # Click on header cart icon
        self.explicitWait(header_link.wait)
        header_link.cartIcon().click()

        # Click on header checkout button
        self.explicitWait(header_link.wait2)
        header_link.proceedToCheckOut().click()

        # Setting up fields on checkout page
        check_out_page.setCompanyName().send_keys(getData["company"])
        check_out_page.setAddressLine1().send_keys(getAddress["address1"])
        check_out_page.setCity().send_keys(getAddress["city"])
        check_out_page.clickStateField().click()
        check_out_page.setState(getAddress["state"])
        check_out_page.setPostalCode().send_keys(getAddress["postalCode"])
        check_out_page.setPhoneNumber().send_keys(InputData().getUserPhoneNumber())

        """
        log.info("Customer {}, {} ordered {} item/s of {} size {} with an SKU of {}".format(
                getData["lastname"], getData["firstname"], getProductInfo["quantity"], getProductInfo["size"],
                getProductInfo["product_name"], product_page.getSKU()))
        """
