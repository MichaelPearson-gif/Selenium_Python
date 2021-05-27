from selenium import webdriver
import time

driver = webdriver.Chrome("../drivers/chromedriver.exe")

driver.set_page_load_timeout(10)

driver.get("https://google.com")

driver.find_element_by_name("q").send_keys("Automation step by step")

driver.find_element_by_class_name("gNO89b").submit()

time.sleep(2)

driver.close()
driver.quit()

print("Test Completed")