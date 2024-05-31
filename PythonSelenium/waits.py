
#demo
'''import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
#Implicit Wait- Global Wait
#driver.implicitly_wait(3)
driver.find_element(By.CLASS_NAME,value="dropbtn").click()
#time.sleep(3)
#driver.find_element(By.LINK_TEXT,value="Facebook").click()
#driver.find_element(By.XPATH,'//a[@href="http://facebook.com"]').click()
wait=WebDriverWait(driver,10)
facebook_option=wait.until(expected_conditions.visibility_of_element_located((By.XPATH,'//a[@href="http://facebook.com"]')))
facebook_option.click()'''

'''import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.zoho.com/signup.html")'''
'''email=driver.find_element(By.ID,value='email')
password=driver.find_element(locate_with(By.TAG_NAME,"input").below(email))
phoneNumber=driver.find_element(locate_with(By.TAG_NAME,"input").below(password))'''
'''wait=WebDriverWait(driver,5)
email=wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//input[@id='email']")))
email.send_keys('suvethajayagopi@gmail.com')
password=wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//input[@id='password']")))
password.send_keys('Suvetha@2002')
phoneNumber=wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//input[@id='rmobile']")))
phoneNumber.send_keys('7339446896')
click_option=wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//span[@class='checked']")))
click_option.click()'''

#zoho signup page automation
'''import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.zoho.com/signup.html")
wait=WebDriverWait(driver,10)
email=driver.find_element(By.ID,value='email')
email.send_keys('suvethajayagopi@gmail.com')
password=driver.find_element(locate_with(By.TAG_NAME,"input").below(email))
password.send_keys('Suvetha@2002')
phoneNumber=driver.find_element(locate_with(By.TAG_NAME,"input").below(password))
phoneNumber.send_keys('7339446896')
checkbox_locator = driver.find_element(By.ID,value="signup-termservice").click()
sign_in_button=driver.find_element(By.ID,value="signupbtn").click()
time.sleep(5)'''

#zoho page using explicit waits
'''import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
driver=webdriver.Chrome()
driver.maximize_window()
wait=WebDriverWait(driver,10)
driver.get("https://www.zoho.com/signup.html")
sends=wait.until(expected_conditions.visibility_of_element_located((By.ID,"email")))
sends.send_keys("jkrose1@gmail.com")
sends1=wait.until(expected_conditions.visibility_of_element_located((By.ID,"password")))
sends1.send_keys("roshini1")
sends3=wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME,"zpassword-show"))).click()
sends2=wait.until(expected_conditions.visibility_of_element_located((By.ID,"rmobile")))
sends2.send_keys("6383552314")
sends3=wait.until(expected_conditions.visibility_of_element_located((By.ID,"signup-termservice"))).click()
sends4=wait.until(expected_conditions.visibility_of_element_located((By.ID,"signupbtn"))).click()'''

#need to do in implicit//orange pge automation
'''import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
wait=WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,"input[placeholder*='Username']"))).send_keys("Admin")
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,"input[placeholder*='Password']"))).send_keys("admin123")
wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//button[@type='submit']"))).click()
time.sleep(5)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,"p.oxd-userdropdown-name"))).click()
time.sleep(5)
wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"(//a[@class='oxd-userdropdown-link'])[4]"))).click()
time.sleep(5)'''

#automation from login to logout
'''import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
wait=WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,"input[placeholder*='Username']"))).send_keys("Admin")
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,"input[placeholder*='Password']"))).send_keys("admin123")
wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//button[@type='submit']"))).click()
wait=WebDriverWait(driver,5)
wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"(//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'])[1]"))).click()
wait=WebDriverWait(driver,5)
wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[2]"))).send_keys("Admin")
time.sleep(5)
wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"(//button[@type='submit'])"))).click()
time.sleep(5)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,"p.oxd-userdropdown-name"))).click()
time.sleep(5)
wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"(//a[@class='oxd-userdropdown-link'])[4]"))).click()
time.sleep(5)'''

#invisibility_of_element_located
'''import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
driver=webdriver.Chrome()
driver.maximize_window()
wait=WebDriverWait(driver,10)
driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
driver.find_element(By.XPATH,"//button[text()='Start']").click()
time.sleep(5)
wait.until(expected_conditions.invisibility_of_element_located((By.ID,'loading')))
text_visible=driver.find_element(By.ID,"finish").text
time.sleep(5)
print(text_visible)'''

#fluent wait
'''import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
driver.find_element(By.CLASS_NAME,"dropbtn").click()
wait=WebDriverWait(driver,timeout=30,poll_frequency=5,ignored_exceptions=[NoSuchElementException])
facebook_option=wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT,"Facebook")))
facebook_option.click()'''

#actionschain-keyboard
'''import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver import Keys
driver=webdriver.Chrome()
driver.maximize_window()'''
'''action=ActionChains(driver)
driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")
time.sleep(5)
driver.find_element(By.ID,value="input-email").send_keys("suvethajayagopi@gmail.com")
driver.find_element(By.ID,value="input-password").send_keys("Suvetha@1317")
action.send_keys(Keys.ENTER).perform()
time.sleep(3)'''
'''driver.get("https://omayo.blogspot.com/")
links=driver.find_elements(By.XPATH,value="//div[@id='LinkList1']//a")
print(len(links))
for link in links:
    print(link.get_attribute("href"))
for link in links:
    action=ActionChains(driver)
    action.key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL).perform()
time.sleep(5)'''

#automation of registeration page
'''import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver import ActionChains
from selenium.webdriver import Keys
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")
action=ActionChains(driver)
driver.implicitly_wait(3)
driver.find_element(By.LINK_TEXT,"Register").click()
time.sleep(3)
driver.find_element(By.ID,'input-firstname').send_keys("Suvetha")
driver.find_element(By.ID,'input-lastname').send_keys("J")
driver.find_element(By.ID,'input-email').send_keys("suvethajayagopi@gmail.com")
telephone=driver.find_element(By.ID,'input-telephone')
telephone.send_keys("7339446896")
password=driver.find_element(locate_with(By.ID,'input-password').below(telephone))
password.send_keys("Suvetha@13")
password_confirm=driver.find_element(locate_with(By.ID,'input-confirm').below(password))
password_confirm.send_keys("Suvetha@13")
wait=WebDriverWait(driver,5)
wait.until(expected_conditions.element_to_be_clickable((By.XPATH,"(//input[@type='radio'])[3]"))).click()
driver.find_element(By.XPATH,"(//input[@type='checkbox'])").click()
action.send_keys(Keys.ENTER).perform()
time.sleep(3)'''

#login automation using actionchains
'''import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver import Keys
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://smartclifflms.info/login/index.php?testsession=564")
action=ActionChains(driver)
driver.find_element(By.ID,"username").send_keys("suvetha_cj-i")
driver.find_element(By.ID,"password").send_keys("Welcome@123")
action.send_keys(Keys.ENTER).perform()
time.sleep(5)'''

#actionchains on keyboard
'''import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver import Keys
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.edzola.com/home")
#links=driver.find_elements(By.XPATH,value="//div[@id='comp-itmmthpi']//a")
#links=driver.find_elements(By.CSS_SELECTOR,value="div#comp-itmmthpi a")
links=driver.find_elements(By.CSS_SELECTOR,value="div.CJF7A2 a")
print(len(links))
for link in links:
    print(link.get_attribute("href"))
for link in links:
    action=ActionChains(driver)
    action.key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL).perform()
for link in links:
    link.click()
time.sleep(20)'''

'''import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver import Keys
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
actions=ActionChains(driver)'''
#move to
'''blogs=driver.find_element(By.ID,"blogsmenu")
actions.move_to_element(blogs).perform()
click1=driver.find_element(By.XPATH,"//span[text()='SeleniumOneByArun']")
actions.click(click1).perform()
driver.implicitly_wait(5)
driver.back()
blogs = driver.find_element(By.ID, "blogsmenu")
actions.move_to_element(blogs).perform()
click2=driver.find_element(By.XPATH,"//span[text()='Selenium143']")
actions.click(click2).perform()'''
#double click
'''doubleclick=driver.find_element(By.XPATH,'//button[text()=" Double click Here   "]')
actions.double_click(doubleclick).perform()'''
#context click-right click
'''rightclick=driver.find_element(By.XPATH,'//button[text()=" Double click Here   "]')
actions.context_click(rightclick).perform()'''
#time.sleep(3)

#drag and drop
'''import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
driver=webdriver.Chrome()
driver.maximize_window()
actions=ActionChains(driver)
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
time.sleep(5)
box1=driver.find_element(By.ID,"box6")
box2=driver.find_element(By.ID,"box106")
#actions.drag_and_drop(box1,box2).perform()
actions.click_and_hold(box1) \
       .move_to_element(box2) \
       .release(box2) \
       .perform()
time.sleep(5)'''















