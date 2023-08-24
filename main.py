import time
import unittest
import random
import string
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By


class CourseHunterTest(unittest.TestCase):

    @allure.step
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.base_url = "https://coursehunter.net/"

    @allure.step
    def test_register(self):
        driver = self.driver
        self.open_home_page(driver)
        self.sign_up(driver)
        get_title = driver.title
        self.assertEqual(get_title, "Sign up success | CourseHunter")

    @allure.step
    def test_login(self):
        driver = self.driver
        self.open_home_page(driver)
        self.log_in(driver)
        get_title = driver.title
        print(get_title)
        self.assertEqual(get_title, "Учитесь, Блеать! - Видеокурсы для разработчиков | CourseHunter")

    @staticmethod
    def log_in(driver):
        signInBtn = driver.find_element(By.XPATH, "//a[normalize-space()='Sign in']")
        signInBtn.click()
        emailField = driver.find_element(By.XPATH, "//input[@id='email']")
        emailField.send_keys("4ester31029@gmail.com")
        passField = driver.find_element(By.XPATH, "//input[@id='password']")
        passField.send_keys("taras123")
        sign_inBtn = driver.find_element(By.XPATH, "//button[normalize-space()='Sign in']")
        sign_inBtn.click()
        time.sleep(5)

    @staticmethod
    def sign_up(driver):
        sign_up = driver.find_element(By.XPATH, "//a[normalize-space()='Sign Up']")
        sign_up.click()
        time.sleep(3)
        em = driver.find_element(By.XPATH, "//input[@name='email']")
        for i in range(1):
            ran_email = ''.join(random.sample(string.ascii_lowercase, 8)) + "@gmail.com"
            print(ran_email)
        em.send_keys(ran_email)
        ps = driver.find_element(By.XPATH, "//input[@name='password']")
        ps.send_keys("taras123")
        ps2 = driver.find_element(By.XPATH, "//input[@name='password_confirm']")
        ps2.send_keys("taras123")
        accept = driver.find_element(By.XPATH, "//button[normalize-space()='Sign Up']")
        accept.click()
        time.sleep(3)

    def open_home_page(self, driver):
        driver.get(self.base_url)

    def tearDown(self):
        self.driver.close()
