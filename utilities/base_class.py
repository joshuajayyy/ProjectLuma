import inspect
import logging

import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.product_page import ProductPage


@pytest.mark.usefixtures("invokeBrowser")
class BaseClass:

    def explicitWait(self, eWait):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located(eWait))

    def getlogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler("C:/Users/SLMP - Joshua/PycharmProjects/ProjectLuma/testData/log_file.log")
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)

        logger.setLevel(logging.DEBUG)
        return logger

    @pytest.mark.usefixtures("getProductInfo")
    def totalAmount(self, getProductInfo):
        product_page = ProductPage(self.driver)
        total = product_page.getPrice() * getProductInfo["quantity"]
        return total
