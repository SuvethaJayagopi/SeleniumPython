#execute script alert
'''import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://bstackdemo.com/")
#driver.execute_script("alert('Welcome')")
#driver.execute_script("prompt('Enter your name')")
driver.execute_script("confirm('Are you Quit')")
time.sleep(3)'''

#click element using js executor
'''import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
'''#method1
'''driver.execute_script("document.getElementById('alert1').click()")
time.sleep(3)'''
#method2
'''button=driver.find_element(By.ID,'alert1')
driver.execute_script("arguments[0].click()",button)
time.sleep(4)'''

#code reusability
'''import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://bstackdemo.com/")
button=driver.find_element(By.XPATH,"//span[text()='Apple']")
bag=driver.find_element(By.XPATH,"//span[@class='bag bag--float-cart-closed']")
def click_elefunction(element):
 driver.execute_script("arguments[0].click()",element)
click_elefunction(button)
time.sleep(3)
click_elefunction(bag)
time.sleep(3)'''

#retrive URL and title
'''import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
#driver.get("https://omayo.blogspot.com/")
driver.get("https://www.google.com/")
web_title=str(driver.execute_script("return document.title"))
print(web_title)
web_URL=str(driver.execute_script("return document.URL"))
print(web_URL)'''

#flashing an element
'''import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
#driver.get("https://omayo.blogspot.com/")
driver.get("https://bstackdemo.com/")
def flash_element(element):
    for i in range(1,25):
     driver.execute_script("arguments[0].style.background='black'",element)
     time.sleep(3)
     default_colour=element.value_of_css_property('color')
     driver.execute_script("arguments[0].style.background='"+default_colour+"'",element)
apple=driver.find_element(By.XPATH,"//span[@class='checkmark'][1]")
flash_element(apple)'''

'''import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
#driver.get("https://omayo.blogspot.com/")
driver.get("https://bstackdemo.com/signin")
driver.execute_script("document.getElementByClassName('css-1wa3eu0-placeholder')
username=driver.find_element(By.XPATH,"//div[text()='Select Username']")
password=driver.find_element(By.XPATH,"//div[text()='Select Password']")
def type_text(element,input_text):
    driver.execute_script("arguments[0].value='"+input_text+"'",element)
type_text(username,"Suvetha")
type_text(password,"Suvetha@13")
button=driver.find_element(By.ID,"login-btn")
def click_elefunction(element):
 driver.execute_script("arguments[0].click()",element)
click_elefunction(button)
time.sleep(3)'''


'''import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver import Keys
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://bstackdemo.com/signin")
uname=driver.find_element(By.XPATH,"//div[text()='Select Username']").click()
uname1=driver.find_element(By.XPATH,"//div[text()='demouser']")
uname1.click()
password=driver.find_element(By.XPATH,"//div[text()='Select Password']").click()
pword1=driver.find_element(By.XPATH,"//div[text()='testingisfun99']")
pword1.click()
#driver.find_element(By.XPATH,"//button[text()='Log In']").click()
button=driver.find_element(By.ID,"login-btn")
def click_elefunction(element):
 driver.execute_script("arguments[0].click()",element)
click_elefunction(button)
time.sleep(5)'''


'''def type_text(element, input_text):
    driver.execute_script("arguments[0].value = '" + input_text + "'", element)
username = driver.find_element(By.XPATH, "//div/div[@id='username']").click()
username.send
password = driver.find_element(By.XPATH, "//div/div[@id='password']")
#type_text(username, "demouser")
#type_text(password, "testingosfun99")
def click_element(element):
    driver.execute_script("arguments[0].click()", element)
button = driver.find_element(By.ID, "login-btn")
click_element(button)
time.sleep(3)'''

#calendar
'''import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://seleniumpractise.blogspot.com/2016/08/how-to-handle-calendar-in-selenium.html")
def type_date(element,date):
    driver.execute_script("arguments[0].value="+date+"",element)
calendar=driver.find_element(By.ID,"datepicker")
type_date(calendar,'05/03/2024')
driver.quit()'''


#scroll- 5 types
'''import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
driver.execute_script("history.go(0)")
time.sleep(5)
driver.execute_script("window.scrollBy(0,500)")
time.sleep(5)
driver.execute_script("history.go(0)")
time.sleep(5)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(5)
driver.execute_script("window.scrollBy(0,-500)")
time.sleep(5)
blogger=driver.find_element(By.XPATH,"//a[text()='Blogger']")
driver.execute_script("arguments[0].scrollIntoView(true);",blogger)
page_text=str(driver.execute_script("return document.documentElement.innerText"))
print(page_text)'''

'''import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://bstackdemo.com/?signin=true")
page_text=str(driver.execute_script("return document.documentElement.innerText"))
print(page_text)
driver.execute_script("history.go(0)")
time.sleep(5)
driver.execute_script("window.scrollBy(0,1000)")
time.sleep(5)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(5)
element=driver.find_element(By.XPATH,"(//div[@class='shelf-item__thumb'])[20]")
driver.execute_script("arguments[0].scrollIntoView(true);",element)
time.sleep(3)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(5)'''


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
# Flashing an element
driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")
def flash_element (element):
    for i in range(1, 30):
       driver.execute_script("arguments[0].style.background='red'",element)
       time.sleep(.2)
       default_color = element.value_of_css_property('color')
       driver.execute_script("arguments[0].style.background='"+default_color+"'",element)
login_button = driver.find_element(By.XPATH, value="//input[@type='submit']")
flash_element(login_button)
time.sleep(4)



