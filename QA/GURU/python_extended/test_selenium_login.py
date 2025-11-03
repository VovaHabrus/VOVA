from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import os

url = "file://" + os.path.abspath("login.html")


@pytest.fixture(scope="function", autouse=True)
def setup_teardown():
    options = Options()
    # options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 5)
    driver.get(url)
    yield driver, wait
    driver.quit()


def test_successful_login(setup_teardown):
    driver, wait = setup_teardown
    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("admin")
    driver.find_element(By.ID, "loginButton").click()

    message = wait.until(EC.visibility_of_element_located((By.ID, "message")))
    assert "Login successful!" in message.text
    assert "success" in message.get_attribute("class")

    login_container = driver.find_element(By.CLASS_NAME, "login-container")
    wait.until(EC.invisibility_of_element(login_container))
    assert not login_container.is_displayed()

    greeting = driver.find_element(By.ID, "greeting")
    assert greeting.text == "Welcome, admin!"

    logout_button = driver.find_element(By.ID, "logoutButton")
    assert logout_button.is_displayed()


def test_successful_login_with_enter(setup_teardown):
    driver, wait = setup_teardown
    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys(Keys.RETURN)

    message = wait.until(EC.visibility_of_element_located((By.ID, "message")))
    assert "Login successful!" in message.text
    assert "success" in message.get_attribute("class")

    login_container = driver.find_element(By.CLASS_NAME, "login-container")
    wait.until(EC.invisibility_of_element(login_container))
    assert not login_container.is_displayed()

    greeting = driver.find_element(By.ID, "greeting")
    assert greeting.text == "Welcome, admin!"

    logout_button = driver.find_element(By.ID, "logoutButton")
    assert logout_button.is_displayed()


def test_empty_username(setup_teardown):
    driver, wait = setup_teardown
    driver.find_element(By.ID, "password").send_keys("admin")
    driver.find_element(By.ID, "loginButton").click()

    message = wait.until(EC.visibility_of_element_located((By.ID, "message")))
    assert "Username is required." in message.text
    assert "error" in message.get_attribute("class")


def test_empty_password(setup_teardown):
    driver, wait = setup_teardown
    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "loginButton").click()

    message = wait.until(EC.visibility_of_element_located((By.ID, "message")))
    assert "Password is required." in message.text
    assert "error" in message.get_attribute("class")


def test_empty_username_and_password(setup_teardown):
    driver, wait = setup_teardown
    driver.find_element(By.ID, "loginButton").click()

    message = wait.until(EC.visibility_of_element_located((By.ID, "message")))
    assert "Username and Password are required." in message.text
    assert "error" in message.get_attribute("class")


def test_invalid_credentials(setup_teardown):
    driver, wait = setup_teardown
    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("wrongpassword")
    driver.find_element(By.ID, "loginButton").click()

    message = wait.until(EC.visibility_of_element_located((By.ID, "message")))
    assert "Invalid username or password." in message.text
    assert "error" in message.get_attribute("class")


def test_logout(setup_teardown):
    driver, wait = setup_teardown
    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("admin")
    driver.find_element(By.ID, "loginButton").click()

    logout_button = wait.until(EC.element_to_be_clickable((By.ID, "logoutButton")))
    logout_button.click()

    login_container = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "login-container")))
    assert login_container.is_displayed()

    greeting = driver.find_element(By.ID, "greeting")
    assert greeting.text == ""

    assert not logout_button.is_displayed()
