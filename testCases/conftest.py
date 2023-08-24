import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#add command line argument browser
def pytest_addoption(parser):
    parser.addoption("--browser")

#get the passed value to cmd line arg
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver_path = "E:\Ashlesha\Drivers\chromedriver.exe"
        #service_obj = Service(driver_path)
        driver = webdriver.Chrome()

    elif browser == "firefox":
        driver = webdriver.Firefox()

    elif browser == "edge":
        driver = webdriver.Edge()

    else:
        driver_path = "E:\Ashlesha\Drivers\chromedriver.exe"
        ch_options = webdriver.ChromeOptions()
        ch_options.add_argument("headless")
        driver = webdriver.Chrome(options = ch_options)

    driver.get("https://iemodemoindia.meditab.com/#/login")
    driver.maximize_window()
    time.sleep(5)
    return driver


@pytest.fixture(params= [("abcd", "ashlesha","Neha@7276")])
def login_credentials(request):
    return request.param

def pytest_configure(config):
    config._metadata = {
        "username": "Ashlesha Zambare",
        "Project": "DrCatalyst_EHR",
        "Test" : "Login"
    }


