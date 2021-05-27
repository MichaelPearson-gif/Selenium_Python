from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import HtmlTestRunner

class GoogleSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_search_automation(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("Automation")
        self.driver.find_element_by_class_name("gNO89b").submit()
        print(self.driver.title)

    def test_search_name(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("Michael Pearson")
        self.driver.find_element_by_class_name("gNO89b1").submit()
        print(self.driver.title)


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./reports'), verbosity=2)