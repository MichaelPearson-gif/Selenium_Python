from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from AutomationFramework_1.pages.loginPage import LoginPage
from AutomationFramework_1.pages.homePage import HomePage
from AutomationFramework_1.utils import utils
import time

@pytest.mark.usefixtures("test_setup")
class TestLogin():

    def test_login(self):
        driver = self.driver
        driver.get(utils.URL)

        login = LoginPage(driver)
        login.enter_username(utils.USERNAME)
        login.enter_password(utils.PASSWORD)
        time.sleep(2)
        login.click_login()

    def test_logout(self):
        driver = self.driver
        homePage = HomePage(driver)
        homePage.click_welcome()
        homePage.click_logout()

