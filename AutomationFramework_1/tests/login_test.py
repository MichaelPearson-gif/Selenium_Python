from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from AutomationFramework_1.pages.loginPage import LoginPage
from AutomationFramework_1.pages.homePage import HomePage
from AutomationFramework_1.utils import utils

class TestLogin():

    @pytest.fixture(scope="class")
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.implicitly_wait(5)
        driver.maximize_window()
        yield
        driver.close()
        driver.quit()
        print("Test completed")

    def test_login(self, test_setup):
        driver.get(utils.URL)

        login = LoginPage(driver)
        login.enter_username(utils.USERNAME)
        login.enter_password(utils.PASSWORD)
        login.click_login()

    def test_logout(self, test_setup):
        homePage = HomePage(driver)
        homePage.click_welcome()
        homePage.click_logout()

