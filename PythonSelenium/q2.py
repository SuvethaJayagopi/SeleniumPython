import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
driver=webdriver.Chrome()
driver.get("https://www.gmail.com")
driver.maximize_window()
wait=WebDriverWait(driver,10)
page_title = wait.until(expected_conditions.title_is("Gmail"))
username = wait.until(expected_conditions.visibility_of_element_located((By.ID, "identifierId")))
status=username.is_displayed()
if(status):
    print("True")
status1=username.is_enabled()
if(status1):
    print("True")
tag_name=username.tag_name
print(tag_name)
attribute_name=username.get_attribute("id")
print(attribute_name)
css_value = username.value_of_css_property('color')
print("Height CSS value:", css_value)
username.send_keys("abc123")
username.clear()
username.send_keys("2k20ece078@kiot.ac.in")
wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//span[text()='Next']"))).click()
password_textbox=wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//input[@type='password']")))
password_textbox.send_keys("Suvetha@2002")
wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//span[text()='Next']"))).click()
compose_button = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//div[text()='Compose']")))
compose_button.click()
time.sleep(5)
driver.quit()



