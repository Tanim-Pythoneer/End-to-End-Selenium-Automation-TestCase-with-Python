import time

import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path='/Users/tanimkamal/Downloads/chromedriver 2')

    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path='/Users/tanimkamal/Downloads/geckodriver')

    elif browser_name == "IE":
        print("IE Driver")

    driver.get("https://liiteri.net/en/home")
    driver.maximize_window()

    request.cls.driver = driver
    yield
    time.sleep(3)
    driver.close()
