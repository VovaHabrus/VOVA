import allure

from TEST_PRICE.locators.login_page_locators import LoginPageLocators
from TEST_PRICE.pages.base_page import BasePage


class LoginPage(BasePage):
    locators = LoginPageLocators()

    @allure.step("Fill login fields")
    def fill_login_fields(self):
        self.element_is_visible(self.locators.LOGIN_BTN).click()
        self.element_is_visible(self.locators.EMAIL)
        self.element_is_visible(self.locators.PASSWORD)
        self.element_is_visible(self.locators.SUBMIT_BTN).click()

    @allure.step("Fill login fields")
    def fill_login_fields_2(self):
        self.driver.element("//a[contains(text(),'Вхід')]").click()
        self.driver.element("#LoginForm_username").type("vova.habrus@gmail.com")
        self.driver.element("#login_user_password").type("PriceTest123")
        self.driver.element(".btn.btn-orange.btn-login").click()
