from selenium.webdriver.common.by import By


class CheckOutPage:

    company_name = (By.CSS_SELECTOR, "input[name='company']")
    address_line_1 = (By.CSS_SELECTOR, "input[name='street[0]']")
    city = (By.CSS_SELECTOR, "input[name='city']")
    click_region_field = (By.CSS_SELECTOR, "select[name='region_id']")
    region = (By.CSS_SELECTOR, "select[name='region_id'] option[data-title]")
    postal_code = (By.CSS_SELECTOR, "input[name='postcode']")
    phone_number = (By.CSS_SELECTOR, "input[name='telephone']")

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
