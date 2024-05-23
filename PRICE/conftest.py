from datetime import datetime
import allure
import pytest
from selenium import webdriver


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    attach = driver.get_screenshot_as_png()
    allure.attach(
        attach,
        name=f"Screenshot {datetime.today()}",
        attachment_type=allure.attachment_type.PNG,
    )
    driver.quit()
