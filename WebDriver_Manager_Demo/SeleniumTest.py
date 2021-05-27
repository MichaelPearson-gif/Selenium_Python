from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

# No longer need an exe file for the chrome driver
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://google.com")
time.sleep(2)
driver.close()
driver.quit