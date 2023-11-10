from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class ProductHover:

    element_to_hover = (By.CSS_SELECTOR, ".product-items .product-item:nth-child(2)")
    size = (By.CSS_SELECTOR, ".size .clearfix .text")
    color = (By.CSS_SELECTOR, ".color .color:nth-child(2)")
    cart = (By.CSS_SELECTOR, ".tocart")
    product_name = (By.CSS_SELECTOR, ".product-item-name")

    def __init__(self, driver):
        self.driver = driver

    def hover_element(self):
        element = self.driver.find_element(*ProductHover.element_to_hover)
        hover = ActionChains(self.driver)
        hover.move_to_element(element).perform()

    def set_size_on_hover(self):
        item = self.driver.find_element(*ProductHover.element_to_hover)
        sizes = item.find_elements(*ProductHover.size)
        for size in sizes:
            if size.text == "S":
                size.click()
                break

    def set_color_on_hover(self):
        item = self.driver.find_element(*ProductHover.element_to_hover)
        item.find_element(*ProductHover.color).click()

    def add_to_cart_on_hover(self):
        item = self.driver.find_element(*ProductHover.element_to_hover)
        return item.find_element(*ProductHover.cart)

    def get_product_hover_name(self):
        item = self.driver.find_element(*ProductHover.element_to_hover)
        product_name = item.find_element(*ProductHover.product_name).text
        return product_name

