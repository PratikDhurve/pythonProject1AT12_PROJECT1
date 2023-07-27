import self as self
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
from selenium.webdriver.common.action_chains import ActionChains

class LoginTest(unittest.TestCase):

    @classmethod
    def setupClass(cls):
        cls.driver_1 = webdriver.Chrome()
        cls.driver_1.implicitly_wait(10)
        cls.driver_1.maximize_window()

    def Test_login_valid(self):
        self.driver_1 = webdriver.Chrome()
        self.driver_1.maximize_window()
        self.driver_1.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver_1.implicitly_wait(20)
        self.driver_1.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
        self.driver_1.implicitly_wait(20)
        self.driver_1.find_element(By.XPATH, "//*[@type='password']").send_keys("admin123")
        self.driver_1.find_element(By.XPATH, "//*[@type='submit']").click()
        self.driver_1.implicitly_wait(20)

    @classmethod
    def tearDownClass(cls):
        print("The User is logged in Successfully")
        cls.driver_1.close()
        cls.driver_1.quit()
