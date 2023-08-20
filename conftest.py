"""This module is used for configuring webdriver."""
from datetime import datetime
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='function')
def driver():
    """Google Chrome is used as driver."""
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    screenshot = driver.get_screenshot_as_png()
    allure.attach(
        body=screenshot,
        name=f'Screenshot {datetime.today()}',
        attachment_type=allure.attachment_type.PNG
    )
    driver.quit()
