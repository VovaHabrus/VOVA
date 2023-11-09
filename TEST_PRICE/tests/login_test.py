import time

import allure
from selene import have, browser

from TEST_PRICE.pages.login_page import LoginPage


@allure.suite("Login page")
class TestElements:
    @allure.feature("Logining")
    class TestTextBox:
        #    @allure.title("Check how Login")
        #    def test_open_login(self, driver):
        #        text_box_page = LoginPage(driver, "https://price.ua/ua")
        #        text_box_page.open()
        #        text_box_page.fill_login_fields_2("vova.habrus@gmail.com")

        @allure.title("Check how Login 2")
        def test_open_login_2(self):
            browser.open("https://price.ua/ua")
            time.sleep(3)
            browser.element("//a[contains(text(),'Вхід')]").click()
            browser.element("#LoginForm_username").type("vova.habrus@gmail.com")
            browser.element("#login_user_password").type("PriceTest123")
            browser.element(".btn.btn-orange.btn-login").click()
            browser.element("a[id='header-user-link'] span").should(have.exact_text("Vovan"))
