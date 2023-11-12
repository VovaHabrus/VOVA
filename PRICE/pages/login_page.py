import time

import allure

from PRICE.locators.login_page_locators import LoginPageLocators
from PRICE.pages.base_page import BasePage


class LoginPage(BasePage):
    locators = LoginPageLocators()

    @allure.step("Fill in all fields")
    def fill_login_fields(self):
        self.element_is_visible(self.locators.EMAIL).send_keys("vova.habrus@gmail.com")
        self.element_is_visible(self.locators.PASSWORD).send_keys("PriceTest123")

    @allure.step("Click on login btn")
    def click_login_btn(self):
        time.sleep(1)
        self.element_is_visible(self.locators.LOGIN_BTN).click()

    @allure.step("Click submint when filled the fields")
    def click_submint_btn(self):
        time.sleep(1)
        self.element_is_visible(self.locators.SUBMIT_BTN).click()
