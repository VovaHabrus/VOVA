import time

import allure
from selene import browser, have

from PRICE_SELENE.pages.login_page_mod import fill_fild


@allure.title("Test valid login")
def test_valid_login():
    browser.open("https://price.ua/ua")
    time.sleep(3)
    browser.element("//a[contains(text(),'Вхід')]").click()
    fill_fild()
    browser.element(".btn.btn-orange.btn-login").click()
    browser.element("a[id='header-user-link'] span").should(have.exact_text("Vovan"))


@allure.title("Test catagoris")
def test_category():
    browser.open("https://price.ua/ua")
    time.sleep(3)
