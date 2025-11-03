import os

import pytest
from playwright.sync_api import sync_playwright

url = "file://" + os.path.abspath("login.html")


@pytest.fixture(scope="function", autouse=True)
def setup_teardown():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.set_default_timeout(5000)
        page.goto(url)
        yield page
        page.close()
        browser.close()


def test_successful_login(setup_teardown):
    page = setup_teardown
    page.fill("#username", "admin")
    page.fill("#password", "admin")
    page.click("#loginButton")

    assert page.is_visible("#message")
    assert "Login successful!" in page.inner_text("#message")
    assert "success" in page.get_attribute("#message", "class")

    page.wait_for_selector(".login-container", state="hidden")
    assert not page.is_visible(".login-container")
    assert page.inner_text("#greeting") == "Welcome, admin!"
    assert page.is_visible("#logoutButton")


def test_successful_login_with_enter(setup_teardown):
    page = setup_teardown
    page.fill("#username", "admin")
    page.fill("#password", "admin")
    page.press("#password", "Enter")

    assert page.is_visible("#message")
    assert "Login successful!" in page.inner_text("#message")
    assert "success" in page.get_attribute("#message", "class")

    page.wait_for_selector(".login-container", state="hidden")
    assert not page.is_visible(".login-container")
    assert page.inner_text("#greeting") == "Welcome, admin!"
    assert page.is_visible("#logoutButton")


def test_empty_username(setup_teardown):
    page = setup_teardown
    page.fill("#password", "admin")
    page.click("#loginButton")

    assert page.is_visible("#message")
    assert "Username is required." in page.inner_text("#message")
    assert "error" in page.get_attribute("#message", "class")


def test_empty_password(setup_teardown):
    page = setup_teardown
    page.fill("#username", "admin")
    page.click("#loginButton")

    assert page.is_visible("#message")
    assert "Password is required." in page.inner_text("#message")
    assert "error" in page.get_attribute("#message", "class")


def test_empty_username_and_password(setup_teardown):
    page = setup_teardown
    page.click("#loginButton")

    assert page.is_visible("#message")
    assert "Username and Password are required." in page.inner_text("#message")
    assert "error" in page.get_attribute("#message", "class")


def test_invalid_credentials(setup_teardown):
    page = setup_teardown
    page.fill("#username", "admin")
    page.fill("#password", "wrongpassword")
    page.click("#loginButton")

    assert page.is_visible("#message")
    assert "Invalid username or password" in page.inner_text("#message")
    assert "error" in page.get_attribute("#message", "class")


def test_logout(setup_teardown):
    page = setup_teardown
    page.fill("#username", "admin")
    page.fill("#password", "admin")
    page.click("#loginButton")

    page.wait_for_selector("#logoutButton")
    assert page.is_visible("#logoutButton")

    page.click("#logoutButton")

    page.wait_for_selector(".login-container", state="visible")
    assert page.is_visible(".login-container")
    assert page.inner_text("#greeting") == ""
    assert not page.is_visible("#logoutButton")
