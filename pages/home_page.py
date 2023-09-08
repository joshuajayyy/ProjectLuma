from selenium.webdriver.common.by import By


class HomePage:

    scroll = (By.CSS_SELECTOR, "h2[class='title']")

    def __init__(self, driver):
        self.driver = driver


