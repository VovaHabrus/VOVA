import time

import allure
from selene import browser, have


@allure.title("Check how Login 2")
def test_open_website():
    browser.open("https://price.ua/ua")
    time.sleep(3)
    browser.element("//a[contains(text(),'Вхід')]").click()
    browser.element("#LoginForm_username").type("vova.habrus@gmail.com")
    browser.element("#login_user_password").type("PriceTest123")
    browser.element(".btn.btn-orange.btn-login").click()
    browser.element("a[id='header-user-link'] span").should(have.exact_text("Vovan"))
