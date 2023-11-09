from selene import browser
from selene import by


def test_open_website():
    browser.open("http://localhost/dashboard/")
    # browser.element(by.xpath("//a[contains(text(),'Вхід')]")).click()
