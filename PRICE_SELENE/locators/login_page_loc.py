from selenium.webdriver.common.by import By


class LoginPageLocators:
    # form fields
    EMAIL = (By.XPATH, "//input[@id='LoginForm_username']")
    PASSWORD = (By.XPATH, "//input[@id='login_user_password']")