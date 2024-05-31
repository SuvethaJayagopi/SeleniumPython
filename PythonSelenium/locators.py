#by id
'''import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.leafground.com/input.xhtml")
element = driver.find_element(By.ID, value="j_idt88:name").send_keys("Suvetha")
time.sleep(5)'''

'''import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/ ")
element = driver.find_element(By.ID,"ta1").send_keys("I am here")
time.sleep(5)'''

#by name
'''import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.co.in ")
element = driver.find_element(By.NAME,"q").send_keys("suvetha")
time.sleep(5)'''

'''import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
element = driver.find_element(By.NAME,"samename").click()
time.sleep(5)'''

#by classname
'''import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/")
element = driver.find_element(By.CLASS_NAME,value="banner-image").click()
time.sleep(5)'''

'''import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
element = driver.find_element(By.CLASS_NAME,value="dropbtn").click()
time.sleep(5)'''

#by tag name
'''import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.leafground.com/select.xhtml")
element = driver.find_element(By.TAG_NAME,value="select").click()
time.sleep(5)'''

#by linktext
'''import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.flipkart.com/")
element = driver.find_element(By.LINK_TEXT,value="Login").click()
time.sleep(10)'''

#by partial link text
'''import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
element = driver.find_element(By.PARTIAL_LINK_TEXT,value="Sel").click()
time.sleep(10)'''

#absolute path
'''import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
element = driver.find_element(By.XPATH,value="/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[1]/div/div/div[2]/div[1]/textarea").send_keys("suvetha")
time.sleep(10)'''

#relative path
'''import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
element = driver.find_element(By.XPATH,value='//*[@id="ta1"]').send_keys("suvetha")
time.sleep(10)'''

#locator functionality
'''from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://neilpatel.com/ubersuggest/")
#element = driver.find_element(By.XPATH,value='//*[@name="keyword"]').send_keys("Marketing")
#element = driver.find_element(By.XPATH,value='//input[@type="text"]').send_keys("Marketing")
#element = driver.find_element(By.XPATH,value='//input[text()="text"]').send_keys("Marketing")
#element = driver.find_element(By.XPATH, '//input[contains(@placeholder, "Enter")]').send_keys("Marketing")'''


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.zoho.com/signup.html")
#above
'''phoneNumber=driver.find_element(By.ID,value='rmobile')
password=driver.find_element(locate_with(By.TAG_NAME,"input").above(phoneNumber))
phoneNumber.send_keys('7339446896')
password.send_keys('1317')'''
#below
'''email=driver.find_element(By.ID,value='email')
password=driver.find_element(locate_with(By.TAG_NAME,"input").below(email))
email.send_keys('suve')
password.send_keys('1317')'''
#to left of
'''linkedIn=driver.find_element(By.CLASS_NAME,value='vi-linkedin')
google=driver.find_element(locate_with(By.TAG_NAME,"span").to_left_of(linkedIn)).click()
time.sleep(5)'''
#to right of
'''linkedIn=driver.find_element(By.CLASS_NAME,value='vi-linkedin')
microsoft=driver.find_element(locate_with(By.TAG_NAME,"span").to_right_of(linkedIn)).click()
time.sleep(5)'''
#near
'''linkedIn=driver.find_element(By.CLASS_NAME,value='vi-linkedin')
microsoft=driver.find_element(locate_with(By.TAG_NAME,"span").near(linkedIn)).click()
time.sleep(5)'''
#checkbox


'''email=driver.find_element(By.ID,value='email')
password=driver.find_element(locate_with(By.TAG_NAME,"input").below(email))
phoneNumber=driver.find_element(locate_with(By.TAG_NAME,"input").below(password))
email.send_keys('suvethajayagopi@gmail.com')
password.send_keys('Suve1317')
phoneNumber.send_keys('7339446896')
signup=driver.find_element(By.CLASS_NAME,value='signupbtn').click()
time.sleep(5)'''
#css selector
'''driver.find_element(By.CSS_SELECTOR, value="input#email").send_keys('suvethajayagopi@gmail.com')
time.sleep(5)'''

#starts with
'''driver.find_element(By.CSS_SELECTOR, value="input[name^=em]").send_keys('suvethajayagopi@gmail.com')
time.sleep(5)'''

#ends with
'''driver.find_element(By.CSS_SELECTOR, value="input[name$=ail]").send_keys('suvethajayagopi@gmail.com')
time.sleep(5)'''

#contains
driver.find_element(By.CSS_SELECTOR, value="input[name*='email']").send_keys('suvethajayagopi@gmail.com')
time.sleep(5)















