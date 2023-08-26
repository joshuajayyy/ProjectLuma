import pytest

from pages.create_account import CreateAccountPage
from testData.input_data import InputData
from utilities.base_class import BaseClass


class TestAccountPage(BaseClass):

    @pytest.mark.usefixtures("getData")
    def test_createAnAccount(self, getData):
        log = self.getlogger()
        create_account = CreateAccountPage(self.driver)
        create_account.clickCreatebutton().click()
        create_account.setFirstName().send_keys(getData["firstname"])
        create_account.setLastName().send_keys(getData["lastname"])
        create_account.setEmail().send_keys(getData["email"])
        create_account.setPassword().send_keys(getData["password"])
        create_account.setPasswordConfirmation().send_keys(getData["password"])
        create_account.clickSubmitButton().click()
        self.explicitWait(create_account.grab_success_message)
        InputData().logData()
        assert "Thank you for registering with Main Website Store." == create_account.grabSuccessMessage()

        log.info("User with an email address " + getData["email"] + ", " + "Successfully created an account.")
