from selenium.webdriver.common.by import By

from utilities.base_class import BaseClass


class CheckOutPage(BaseClass):

    company_name = (By.CSS_SELECTOR, "input[name='company']")
    address_line_1 = (By.CSS_SELECTOR, "input[name='street[0]']")
    city = (By.CSS_SELECTOR, "input[name='city']")
    click_region_field = (By.CSS_SELECTOR, "select[name='region_id']")
    region = (By.CSS_SELECTOR, "select[name='region_id'] option[data-title]")
    postal_code = (By.CSS_SELECTOR, "input[name='postcode']")
    phone_number = (By.CSS_SELECTOR, "input[name='telephone']")
    radio_button = (By.CSS_SELECTOR, "input[value='flatrate_flatrate']")
    table = (By.CSS_SELECTOR, ".table-checkout-shipping-method tbody .row")
    shipping_method_price = None

    def __init__(self, driver, getStates):
        self.driver = driver
        self.getStates = getStates

    def setCompanyName(self):
        return self.driver.find_element(*CheckOutPage.company_name)

    def setAddressLine1(self):
        return self.driver.find_element(*CheckOutPage.address_line_1)

    def setCity(self):
        return self.driver.find_element(*CheckOutPage.city)

    def clickStateField(self):
        return self.driver.find_element(*CheckOutPage.click_region_field)

    def setState(self, stateAbbrevation):
        a = self.getStates[stateAbbrevation]
        states = self.driver.find_elements(*CheckOutPage.region)
        for state in states:
            b = state.get_attribute("data-title")
            if a == b:
                state.click()
                break

    def setPostalCode(self):
        return self.driver.find_element(*CheckOutPage.postal_code)

    def setPhoneNumber(self):
        return self.driver.find_element(*CheckOutPage.phone_number)

    def setShippingMethod(self):
        methods = self.driver.find_elements(*CheckOutPage.table)
        for method in methods:
            a = method.find_element(By.CSS_SELECTOR, ".table-checkout-shipping-method tbody .row td:nth-child(3)").text
            if a == "Fixed":
                self.shipping_method_price = method.find_element(By.CSS_SELECTOR, ".table-checkout-shipping-method tbody .row td:nth-child(2)").text
                method.find_element(By.CSS_SELECTOR, ".table-checkout-shipping-method tbody .row td:nth-child(1)").click()
                break

        self.shipping_method_price = self.convertPrice(self.shipping_method_price)