import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("invokeBrowser")
class BaseClass:

    def explicit_wait_visibility(self, e_wait):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.visibility_of_element_located(e_wait))

    def explicit_wait_invisibility(self, e_wait):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.invisibility_of_element_located(e_wait))

    def convertPrice(self, convert):
        return float(convert.replace('$', '').replace(',', '').replace('-', ''))

    def execute_scroll_view(self, holder):
        element = self.driver.find_element(*holder)
        self.driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth' });", element)

    def getlogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler("C:/Users/SLMP - Joshua/PycharmProjects/ProjectLuma/testData/log_file.log")
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)

        logger.setLevel(logging.DEBUG)
        return logger