import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.kayak.co.in/")
#element = driver.find_element(By.CLASS_NAME,value="sign-in-nav-link").click()
#element = driver.find_element(By.XPATH,value='//div[text()="Sign in"]').click()
#element = driver.find_element(By.XPATH,value='//*[@class="sign-in-nav-link"]').click()
#element = driver.find_element(By.XPATH,value='//div[@class='sign-in-nav-link']/parent::div.click()
time.sleep(5)