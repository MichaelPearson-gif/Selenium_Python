import unittest
from unittest.runner import TextTestRunner
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import HtmlTestRunner


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

    def test_search_1(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("Automation step by step")
        self.driver.find_element_by_class_name("gNO89b").submit()
        x = self.driver.title
        print(x)
        self.assertEqual(x, "Automation step by step - Google Search")

    def test_search_2(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("Michael Pearson")
        self.driver.find_element_by_class_name("gNO89b").submit()
        x = self.driver.title
        print(x)
        self.assertEqual(x, "Michael Pearson - Google Search")

    @unittest.skip("This is a skipped test.")
    def test_skip(self):
        """ This test should be skipped. """
        pass



if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/18587/OneDrive/Desktop/Git/Selenium_Python/Selenium/reports'), verbosity=2)