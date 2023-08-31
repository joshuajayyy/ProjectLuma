from selenium.webdriver.common.by import By

from utilities.base_class import BaseClass


class PlaceOrderPage(BaseClass):

    s_total = (By.CSS_SELECTOR, ".sub .amount .price")
    d_price = (By.CSS_SELECTOR, ".discount .amount .price")
    ship_price = (By.CSS_SELECTOR, ".shipping .amount .price")
    t_order = (By.CSS_SELECTOR, ".grand .amount .price")
    place_order_button = (By.CSS_SELECTOR, ".primary .checkout")
    wait = (By.CSS_SELECTOR, "body[data-container='body'] .loading-mask .loader")

    def __init__(self, driver):
        self.driver = driver

    def getSubTotalPrice(self):
        sub_total = self.driver.find_element(*PlaceOrderPage.s_total).text
        return self.convertPrice(sub_total)

    def getDiscountPice(self):
        discount_price = self.driver.find_element(*PlaceOrderPage.d_price).text
        return self.convertPrice(discount_price)

    def getShippingPrice(self):
        shipping_price = self.driver.find_element(*PlaceOrderPage.ship_price).text
        return self.convertPrice(shipping_price)

    def getTotalOrderPrice(self):
        total_price = self.driver.find_element(*PlaceOrderPage.t_order).text
        return self.convertPrice(total_price)

    def computation(self):
        return self.getSubTotalPrice() - self.getDiscountPice() + self.getShippingPrice()

    def clickPlaceOrder(self):
        return self.driver.find_element(*PlaceOrderPage.place_order_button)

