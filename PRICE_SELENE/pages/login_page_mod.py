from selene import browser
from PRICE_SELENE.locators.login_page_loc import LoginPageLocators


def fill_fild():
    browser.element("#LoginForm_username").type("vova.habrus@gmail.com")
    browser.element("#login_user_password").type("PriceTest123")
