import os

import pytest
from selenium import webdriver

from testData.input_data import InputData

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", default="chrome"
    )


@pytest.fixture(scope="class")
def invokeBrowser(request):
    global driver

    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=chrome_options)

    elif browser_name == "firefox":
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument("--start-maximized")
        driver = webdriver.Firefox(options=firefox_options)

    driver.get("https://magento.softwaretestingboard.com/")
    driver.implicitly_wait(5)
    request.cls.driver = driver

    yield
    driver.close()


@pytest.fixture(params=InputData.create_account_data, scope="function")
def getData(request):
    return request.param


@pytest.fixture(params=InputData.selected_product, scope="function")
def getProductInfo(request):
    return request.param


@pytest.fixture(params=InputData.random_name_address, scope="function")
def getAddress(request):
    return request.param


@pytest.fixture(params=InputData.states, scope="function")
def getStates(request):
    return request.param


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    screenshot_directory = "C:/Users/SLMP - Joshua/PycharmProjects/ProjectLuma/reports"
    file_path = os.path.join(screenshot_directory, name)
    driver.get_screenshot_as_file(file_path)
