import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.co.in")
time.sleep(2)
print("The Title of the page is",driver.title)
element = driver.find_element(By.NAME,"q")
status = element.is_enabled()
if status:
    print("Enabled")
    element.send_keys("Selenium")
element1 = driver.find_element(By.CLASS_NAME,"zgAlFc")
status = element1.is_enabled()
if status:
    element1.click()
time.sleep(2)
