from selenium.webdriver.common.by import By


class LoginPageLocators:
    # form fields
    EMAIL = (By.CSS_SELECTOR, '#LoginForm_username')
    PASSWORD = (By.CSS_SELECTOR, '#login_user_password')

    SUBMIT_BTN = (By.CSS_SELECTOR, '.btn.btn-orange.btn-login')
    LOGIN_BTN = (By.CSS_SELECTOR, "//a[contains(text(),'Вхід')]")
