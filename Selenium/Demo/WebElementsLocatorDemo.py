from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://google.com")

search_box = driver.find_element_by_name("q")
search_box.send_keys("Michael")
