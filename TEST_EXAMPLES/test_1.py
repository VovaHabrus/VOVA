import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://ua.sinoptik.ua/")
title_btn = browser.find_element(By.CLASS_NAME, "sLogo")
title_btn.click()
title = browser.find_element(By.TAG_NAME, "a")
time.sleep(3)
assert title.text == "Прогноз погоды"
browser.quit()
