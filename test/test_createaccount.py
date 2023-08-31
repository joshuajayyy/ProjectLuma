import time

import pytest

from pages.create_account import CreateAccountPage
from pages.header_links import HeaderLinks
from testData.input_data import InputData
from utilities.base_class import BaseClass


class TestAccountPage(BaseClass):

    @pytest.mark.usefixtures("getData")
    def test_create_an_account(self, getData):
        log = self.getlogger()
        create_account = CreateAccountPage(self.driver)
        header_link = HeaderLinks(self.driver)

        header_link.clickCreatebutton().click()
        create_account.setFirstName().send_keys(getData["firstname"])
        create_account.setLastName().send_keys(getData["lastname"])
        create_account.setEmail().send_keys(getData["email"])
        create_account.setPassword().send_keys(getData["password"])
        create_account.setPasswordConfirmation().send_keys(getData["password"])
        create_account.clickSubmitButton().click()
        self.explicit_wait_visibility(create_account.grab_message)

        assert "Thank you for registering with Main Website Store." == create_account.grabSuccessMessage()
        log.info("User with an email address " + getData["email"] + ", " + "Successfully created an account.")
        InputData().logData()

