import allure

from TEST_PRICE.pages.login_page import LoginPage


@allure.suite("Home Page")
class TestHomePage:
    @allure.feature("TextBox")
    class TestLoginBox:
        @allure.title("Test how login")
        def test_open_login(self, driver):
            text_box_page = LoginPage(driver, "https://price.ua/ua")
            text_box_page.open()
            text_box_page.click_login_btn()
            text_box_page.fill_login_fields()
            text_box_page.click_submint_btn()
