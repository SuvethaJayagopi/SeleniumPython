#iframe
'''import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://letcode.in/frame")
time.sleep(5)
driver.switch_to.frame("firstFr")
driver.find_element(By.NAME,"fname").send_keys("Suvetha")
driver.find_element(By.NAME,"lname").send_keys("J")
time.sleep(5)
child_frame=driver.find_element(By.XPATH,"//iframe[@class='has-background-white']")
driver.switch_to.frame(child_frame)
driver.find_element(By.NAME,"email").send_keys("suvethajayagopi@gmail.com")
time.sleep(5)
driver.switch_to.parent_frame()
driver.find_element(By.NAME,"fname").clear()
time.sleep(5)
driver.switch_to.default_content()
driver.find_element(By.XPATH,"//a[@id='testing']").click()
time.sleep(5)
driver.quit()'''

#iframe
'''import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_link_target")
time.sleep(5)
driver.switch_to.frame("iframeResult")
driver.find_element(By.XPATH,"//a[text()='Visit W3Schools.com!']").click()
time.sleep(3)
driver.quit()'''

#select
'''import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
select_element=driver.find_element(By.ID,"drop1")
select=Select(select_element)
dropdown=select.options
print(len(dropdown))
for options in dropdown:
    print(options.text)
#select.select_by_visible_text("doc 1")
select.select_by_index(4)
#select.select_by_value("mno")
time.sleep(5)'''

#multiple select
'''import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
select_element=driver.find_element(By.ID,"multiselect1")
select=Select(select_element)
multiselect_options=select.options
print(len(multiselect_options))
for option in multiselect_options:
    print(option.text)
#select.select_by_visible_text("Swift")
#select.select_by_index(0)
#select.select_by_value("audix")
select.deselect_by_index(0)
select.deselect_by_value("audix")
select.deselect_by_visible_text("Volvo")
#select.deselect_all()
select.select_by_visible_text("Swift")
time.sleep(5)'''

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver import Keys
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://bstackdemo.com/")
#method1
select_element=driver.find_element(By.XPATH,"//option[text()='Select']").click()
'''allOptions=driver.find_elements(By.CSS_SELECTOR,value="select option")
#Xpath-//select//option
option="Lowest to highest"
for options in allOptions:
    if options.text.__eq__(option):
        options.click()
        time.sleep(5)
        print("Clicked")
        break'''
#METHOD2
'''option1="Highest to lowest"
dropdown=driver.find_element(By.XPATH,"//select/option[contains(text(),'"+option1+"')]")
dropdown.click()
time.sleep(5)'''

#method3
'''option2=driver.find_element(By.XPATH,"//select")
driver.execute_script("arguments[0].value='highestprice'",option2)'''

#method4
'''driver.find_element(By.XPATH,"//select").send_keys("lowestprice")
time.sleep(5)'''

#method5
element=driver.find_element(By.XPATH,value="//select")
action=ActionChains(driver)
action.move_to_element(element).perform()
customOption=driver.find_element(By.XPATH,"//option[text()='Highest to lowest']")
action.click(customOption).perform()
#customOption.click()
time.sleep(5)