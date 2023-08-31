from selenium.webdriver.common.by import By

from utilities.base_class import BaseClass


class CreateAccountPage(BaseClass):

    first_name = (By.ID, "firstname")
    last_name = (By.ID, "lastname")
    email = (By.ID, "email_address")
    password = (By.ID, "password")
    confirm_password = (By.ID, "password-confirmation")
    click_submit = (By.CSS_SELECTOR, "button[title='Create an Account']")
    grab_message = (By.CSS_SELECTOR, "div[role='alert']")

    def __init__(self, driver):
        self.driver = driver

    def setFirstName(self):
        return self.driver.find_element(*CreateAccountPage.first_name)

    def setLastName(self):
        return self.driver.find_element(*CreateAccountPage.last_name)

    def setEmail(self):
        return self.driver.find_element(*CreateAccountPage.email)

    def setPassword(self):
        return self.driver.find_element(*CreateAccountPage.password)

    def setPasswordConfirmation(self):
        return self.driver.find_element(*CreateAccountPage.confirm_password)

    def clickSubmitButton(self):
        return self.driver.find_element(*CreateAccountPage.click_submit)

    def grabSuccessMessage(self):
        return self.driver.find_element(*CreateAccountPage.grab_message).text
