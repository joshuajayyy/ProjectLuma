from selenium.webdriver.common.by import By

from utilities.base_class import BaseClass


class HeaderLinks(BaseClass):

    click_create_account = (By.LINK_TEXT, "Create an Account")
    login_button = (By.LINK_TEXT, "Sign In")
    whats_new = (By.LINK_TEXT, "What's New")
    cart_icon = (By.CSS_SELECTOR, ".showcart")
    proceed_to_checkout = (By.CSS_SELECTOR, ".checkout")
    wait = (By.CSS_SELECTOR, "div[role='alert']")
    wait2 = (By.CSS_SELECTOR, ".subtotal")
    switch = (By.CSS_SELECTOR, ".header .switch")
    sign_out = (By.LINK_TEXT, "Sign Out")
    mini_cart = (By.CSS_SELECTOR, ".minicart-items-wrapper")
    mini_cart_item_name = (By.CSS_SELECTOR, ".product-item-name")

    def __init__(self, driver):
        self.driver = driver

    def clickWhatsNew(self):
        return self.driver.find_element(*HeaderLinks.whats_new)

    def clickCreatebutton(self):
        return self.driver.find_element(*HeaderLinks.click_create_account)

    def clickLoginButton(self):
        return self.driver.find_element(*HeaderLinks.login_button)

    def cartIcon(self):
        return self.driver.find_element(*HeaderLinks.cart_icon)

    def proceedToCheckOut(self):
        return self.driver.find_element(*HeaderLinks.proceed_to_checkout)

    def headerSwitch(self):
        return self.driver.find_element(*HeaderLinks.switch)

    def clickSignOut(self):
        return self.driver.find_element(*HeaderLinks.sign_out)

    def product_names_on_minicart(self):
        item = self.driver.find_element(*HeaderLinks.mini_cart)
        product_names = item.find_elements(*HeaderLinks.mini_cart_item_name)
        return product_names

