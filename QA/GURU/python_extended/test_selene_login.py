from selene.support.shared import browser
from selene import be, have
import pytest
import os

url = "file://" + os.path.abspath("login.html")


@pytest.fixture(scope="function", autouse=True)
def setup_teardown():
    browser.config.browser_name = 'chrome'
    browser.config.headless = True
    browser.config.timeout = 5
    browser.open(url)
    yield
    browser.quit()


def test_successful_login():
    browser.element("#username").type("admin")
    browser.element("#password").type("admin")
    browser.element("#loginButton").click()

    browser.element("#message").should(have.text("Login successful!")).should(have.css_class("success"))
    browser.element(".login-container").should(be.not_.visible)
    browser.element("#greeting").should(have.text("Welcome, admin!"))
    browser.element("#logoutButton").should(be.visible)


def test_successful_login_with_enter():
    browser.element("#username").type("admin")
    browser.element("#password").type("admin").press_enter()

    browser.element("#message").should(have.text("Login successful!")).should(have.css_class("success"))
    browser.element(".login-container").should(be.not_.visible)
    browser.element("#greeting").should(have.text("Welcome, admin!"))
    browser.element("#logoutButton").should(be.visible)


def test_empty_username():
    browser.element("#password").type("admin")
    browser.element("#loginButton").click()

    browser.element("#message").should(have.text("Username is required.")).should(have.css_class("error"))


def test_empty_password():
    browser.element("#username").type("admin")
    browser.element("#loginButton").click()

    browser.element("#message").should(have.text("Password is required.")).should(have.css_class("error"))


def test_empty_username_and_password():
    browser.element("#loginButton").click()

    browser.element("#message").should(have.text("Username and Password are required.")).should(have.css_class("error"))


def test_invalid_credentials():
    browser.element("#username").type("admin")
    browser.element("#password").type("wrongpassword")
    browser.element("#loginButton").click()

    browser.element("#message").should(have.text("Invalid username or password.")).should(have.css_class("error"))


def test_logout():
    browser.element("#username").type("admin")
    browser.element("#password").type("admin")
    browser.element("#loginButton").click()

    browser.element("#logoutButton").should(be.visible).click()
    browser.element(".login-container").should(be.visible)
    # browser.element("#greeting").should(be.empty)
    browser.element("#logoutButton").should(be.not_.visible)
