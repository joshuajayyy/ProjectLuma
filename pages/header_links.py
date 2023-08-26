from selenium.webdriver.common.by import By

from utilities.base_class import BaseClass


class HeaderLinks(BaseClass):

    whats_new = (By.LINK_TEXT, "What's New")
    cart_icon = (By.CSS_SELECTOR, ".showcart")
    proceed_to_checkout = (By.CSS_SELECTOR, ".checkout")
    wait = (By.CSS_SELECTOR, "div[role='alert']")
    wait2 = (By.CSS_SELECTOR, ".subtotal")

    def __init__(self, driver):
        self.driver = driver

    def clickWhatsNew(self):
        return self.driver.find_element(*HeaderLinks.whats_new)

    def cartIcon(self):
        return self.driver.find_element(*HeaderLinks.cart_icon)

    def proceedToCheckOut(self):
        return self.driver.find_element(*HeaderLinks.proceed_to_checkout)
