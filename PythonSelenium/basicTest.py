'''import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.co.in")
page_title=driver.title
print(page_title)
time.sleep(5)
driver.close()'''


'''import time
from selenium import webdriver
from selenium.webdriver.common.by import By
opts=webdriver.ChromeOptions()
opts.add_argument("--headless")
driver=webdriver.Chrome(options=opts)
driver.maximize_window()
driver.get("https://www.google.co.in") #here google does not support by source
page_title=driver.title
print(page_title)
page_url=driver.current_url
print(page_url)
try:
    p_source = driver.page_source.encode('utf-8', 'ignore').decode('utf-8')
    print("Page Source:", p_source)
except UnicodeEncodeError:
    print("Failed to print page source")
time.sleep(5)
driver.close()'''

'''import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://www.google.co.in")
page_title=driver.title
print(page_title)
print(driver.current_url)
file = open("a.txt", "w", encoding='utf8')
file.write(driver.page_source)
file.close()
time.sleep(5)
driver.close()'''

'''import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.co.in")
time.sleep(5)
driver.get("https://www.flipkart.com/")
driver.back()
time.sleep(5)
driver.forward()
time.sleep(5)'''

'''import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
element = driver.find_element(By.ID, value="but2")
status = element.is_enabled() 
print(status)
driver.save_screenshot("homepage.png")
element = driver.find_element(By.CLASS_NAME, value="widget-content") 
print(element.location)
time.sleep(2)'''

'''from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.get("https://www.google.com")
if "Google" in driver.title:
    print("True")
else:
    print("False")
search_box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "q")))
search_box.send_keys("Selenium")
search_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "btnK")))
search_button.click()
driver.quit()'''


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
driver = webdriver.Chrome()
driver.get("https://www.google.com")
if "Google" in driver.title:
    print("True")
else:
    print("False")
wait = WebDriverWait(driver, 20) 
try:
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "truncate")))
    status = element.is_enabled()
    print(f"Is the element enabled? {status}")
except TimeoutException: 
    print("Failed to find the element within the given time.")

