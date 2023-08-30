from selenium.webdriver.common.by import By

from utilities.base_class import BaseClass


class ProductPage(BaseClass):

    product_name = (By.CSS_SELECTOR, ".base")
    sku = (By.CSS_SELECTOR, "div[itemprop='sku']")
    price = (By.CSS_SELECTOR, ".product-info-price .normal-price span[data-price-type='finalPrice'] .price")
    product_sizes = (By.CSS_SELECTOR, ".swatch-opt .size .clearfix .text")
    product_color = (By.CSS_SELECTOR, ".swatch-opt .color .color:nth-child(2)")
    qty = (By.ID, "qty")
    add_to_cart = (By.ID, "product-addtocart-button")

    def __init__(self, driver):
        self.driver = driver

    def getProductName(self):
        return self.driver.find_element(*ProductPage.product_name).text

    def getSKU(self):
        return self.driver.find_element(*ProductPage.sku).text

    def getPrice(self):
        product_price = self.driver.find_element(*ProductPage.price).text
        return self.convertPrice(product_price)

    def setSize(self, product_size):
        sizes = self.driver.find_elements(*ProductPage.product_sizes)
        for size in sizes:
            if size.text == product_size:
                size.click()
                break

    def setColor(self):
        return self.driver.find_element(*ProductPage.product_color)

    def setQuantity(self):
        self.driver.find_element(*ProductPage.qty).clear()
        return self.driver.find_element(*ProductPage.qty)

    def clickAddToCart(self):
        return self.driver.find_element(*ProductPage.add_to_cart)
