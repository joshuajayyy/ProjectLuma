from selenium.webdriver.common.by import By


class SuccessPage:

    message = (By.CSS_SELECTOR, ".page-main .page-title-wrapper .page-title span[data-ui-id='page-title-wrapper']")
    order_number = (By.CSS_SELECTOR, ".order-number")
    wait = (By.CSS_SELECTOR, ".checkout-success")

    def __init__(self, driver):
        self.driver = driver

    def getMessage(self):
        return self.driver.find_element(*SuccessPage.message).text

    def getOrderNumber(self):
        return self.driver.find_element(*SuccessPage.order_number).text
