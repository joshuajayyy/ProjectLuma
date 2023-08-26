from selenium.webdriver.common.by import By

from utilities.base_class import BaseClass


class LoginPage(BaseClass):

    email = (By.ID, "email")
    password = (By.ID, "pass")
    submit = (By.ID, "send2")

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self):
        return self.driver.find_element(*LoginPage.email)

    def setPassword(self):
        return self.driver.find_element(*LoginPage.password)

    def clickSubmit(self):
        return self.driver.find_element(*LoginPage.submit)
