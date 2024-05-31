import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver import ActionChains
from selenium.webdriver import Keys
driver=webdriver.Chrome()
driver.get("https://www.naukri.com/ ")
action=ActionChains(driver)
driver.maximize_window()
driver.implicitly_wait(5)
register_link=driver.find_element(By.XPATH,"//a[text()='Register']")
status=register_link.is_displayed()
if(status):
    print("True")
status1=register_link.is_enabled()
if(status1):
    print("True")
register_link.click()
name=driver.find_element(By.ID,"name")
status2=name.is_enabled()
text = name.get_attribute("placeholder")
print(text)
name.send_keys("Suvetha")
email=driver.find_element(By.XPATH,"//input[@id='email']").send_keys("suvethajayagopi@gmail.com")
password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys("Suvetha")
mobile_number = driver.find_element(By.XPATH, "//input[@id='mobile']")
mobile_number.send_keys("7339446896")
driver.find_element(By.XPATH, "(//h2[@class='main-3'])[2]").click()
location = driver.find_element(By.CSS_SELECTOR, "input.ddInput")
location.send_keys("Coimbatore")
location.send_keys(Keys.ENTER)
action.send_keys(Keys.ENTER).perform()
time.sleep(5)       
driver.quit()
