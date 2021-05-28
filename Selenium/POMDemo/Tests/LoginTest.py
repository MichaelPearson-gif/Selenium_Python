import sys
import os
# sys.path.append("C:/Users/18587/OneDrive/Desktop/Git/Selenium_Python/Selenium")
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import unittest
from POMDemo.Pages.loginPage import LoginPage
from POMDemo.Pages.homePage import HomePage
import HtmlTestRunner

class LoginTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(10)

    def test_login_valid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")


        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/18587/OneDrive/Desktop/Git/Selenium_Python/Selenium/reports"))