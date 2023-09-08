import time

import pytest

from pages.check_out_page import CheckOutPage
from pages.header_links import HeaderLinks
from pages.login_page import LoginPage
from pages.place_order_page import PlaceOrderPage
from pages.product_page import ProductPage
from pages.success_page import SuccessPage
from pages.whatsnew_page import WhatsNewPage
from testData.input_data import InputData
from utilities.base_class import BaseClass


class TestProcessAnOrder(BaseClass):

    @pytest.mark.usefixtures("getData", "getProductInfo", "getAddress", "getStates")
    def test_process_an_order(self, getData, getProductInfo, getAddress, getStates):
        log = self.getlogger()
        header_link = HeaderLinks(self.driver)
        sign_in = LoginPage(self.driver)
        whats_new = WhatsNewPage(self.driver)
        product_page = ProductPage(self.driver)
        check_out_page = CheckOutPage(self.driver, getStates)
        place_order_page = PlaceOrderPage(self.driver)
        success_page = SuccessPage(self.driver)

        # User Sign In
        header_link.clickLoginButton().click()

        # Enter username and password
        sign_in.setEmail().send_keys(InputData().getUserEmail())
        sign_in.setPassword().send_keys(InputData().getUserPassword())
        sign_in.clickSubmit().click()

        # Click on whats new page
        header_link.clickWhatsNew().click()

        # Navigate to whats new page and add product
        self.explicit_wait_visibility(whats_new.target_element)
        self.execute_scroll_view(whats_new.target_element)
        time.sleep(3)
        whats_new.productSearch(getProductInfo["product_name"])

        # Set all necessary information from product page
        product_page.setSize(getProductInfo["size"])
        product_page.setColor().click()
        product_page.setQuantity().send_keys(getProductInfo["quantity"])
        product_price = product_page.getPrice()
        product_sku = product_page.getSKU()
        product_page.clickAddToCart().click()

        # Click on header cart icon
        self.explicit_wait_visibility(header_link.wait)
        header_link.cartIcon().click()

        # Click on header checkout button
        self.explicit_wait_visibility(header_link.wait2)
        header_link.proceedToCheckOut().click()

        # Setting up fields on checkout page
        check_out_page.setCompanyName().send_keys(getData["company"])
        check_out_page.setAddressLine1().send_keys(getAddress["address1"])
        check_out_page.setCity().send_keys(getAddress["city"])
        check_out_page.clickStateField().click()
        check_out_page.setState(getAddress["state"])
        check_out_page.setPostalCode().send_keys(getAddress["postalCode"])
        check_out_page.setPhoneNumber().send_keys(InputData().getUserPhoneNumber())
        check_out_page.setShippingMethod()
        check_out_page.clickNext().click()

        # Place order page
        try:
            assert place_order_page.getSubTotalPrice() == product_price * getProductInfo["quantity"]
            assert place_order_page.getShippingPrice() == check_out_page.shipping_method_price
            assert place_order_page.getTotalOrderPrice() == place_order_page.computation()
            log.info("Pricing is correct")

        except Exception as e:
            log.error(f"Test failed with exception: {e}")

        self.explicit_wait_invisibility(place_order_page.wait)
        place_order_page.clickPlaceOrder().click()

        self.explicit_wait_visibility(success_page.wait)
        assert "Thank you for your purchase!" == success_page.getMessage()

        log.info("Customer {}, {} successfully ordered {} item/s of {} size {} with an SKU of {}. Order number: {}, recorded!".format(
                InputData().getUserLastName(), InputData().getUserFirstName(), getProductInfo["quantity"], getProductInfo["size"],
                getProductInfo["product_name"], product_sku, success_page.getOrderNumber())
        )

        header_link.headerSwitch().click()
        header_link.clickSignOut().click()
