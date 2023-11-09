import time

from selene import browser, have, by

from TEST_PRICE.pages.login_page import TextBoxPage


# def test_open_website():

def test_open_login_2(driver):
    text_box_page = TextBoxPage(driver, "https://price.ua/ua")
    text_box_page.open()


def test_open_login():
    browser.open("https://price.ua/ua")
    time.sleep(3)
    browser.element("//a[contains(text(),'Вхід')]").click()
    browser.element("#LoginForm_username").type("vova.habrus@gmail.com")
    browser.element("#login_user_password").type("PriceTest123")
    browser.element(".btn.btn-orange.btn-login").click()

    browser.element("a[id='header-user-link'] span").should(have.exact_text("Vovan"))
