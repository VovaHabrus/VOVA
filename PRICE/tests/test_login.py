from datetime import datetime

import allure
import pytest
from selenium import webdriver
from PRICE.pages.login_page import LoginPage
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    attach = driver.get_screenshot_as_png()
    allure.attach(
        attach,
        name=f"Screenshot {datetime.today()}",
        attachment_type=allure.attachment_type.PNG,
    )
    driver.quit()


@allure.suite("Home Page")
class TestHomePage:
    @allure.feature("TextBox")
    class TestLoginBox:
        @allure.title("Test how login")
        def test_open_login(self, driver):
            text_box_page = LoginPage(driver, "https://price.ua/ua")
            text_box_page.open()
            text_box_page.click_login_btn()
            text_box_page.fill_login_fields()
            text_box_page.click_submint_btn()
