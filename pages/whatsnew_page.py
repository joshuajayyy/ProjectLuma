from selenium.webdriver.common.by import By


class WhatsNewPage:

    item_info = (By.CSS_SELECTOR, ".product-item-info")
    item_name = (By.CSS_SELECTOR, ".product-item-name")
    target_element = (By.CSS_SELECTOR, "h2[class='title']")

    def __init__(self, driver):
        self.driver = driver

    def productSearch(self, product_name):
        products = self.driver.find_elements(*WhatsNewPage.item_info)
        for product in products:
            if product.find_element(*WhatsNewPage.item_name).text == product_name:
                product.find_element(*WhatsNewPage.item_name).click()
                break
