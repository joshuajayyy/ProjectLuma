from selenium.webdriver.common.by import By


class AccountPage:

    page_title = (By.CSS_SELECTOR, ".page-title")
    wait = (By.CSS_SELECTOR, ".block-dashboard-info .block-title")

    def __init__(self, driver):
        self.driver = driver

    def get_title_page(self):
        return self.driver.find_element(*AccountPage.page_title).text

