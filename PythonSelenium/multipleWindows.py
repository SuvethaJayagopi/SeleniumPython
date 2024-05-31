'''import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
parent_window=driver.current_window_handle
#single window
driver.find_element(By.LINK_TEXT,"Open a popup window").click()
time.sleep(5)
window_text=driver.find_element(By.XPATH,"//h3[text()='New Window']").text
print(window_text)
#handle multiple windows
driver.find_element(By.LINK_TEXT,"Open a popup window").click()
windowId=driver.window_handles
for s in windowId:
    driver.switch_to.window(s)
    if driver.title.__eq__("New Window"):
        window_text=driver.find_element(By.XPATH,"//h3[text()='New Window']").text
        print(window_text)
        driver.close()
        break
time.sleep(5)
driver.switch_to.window(parent_window)
driver.find_element(By.ID,"ta1").send_keys("Suvetha")
time.sleep(5)'''

'''import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.leafground.com/window.xhtml;jsessionid=node03le8b5xfiuzw6c8bmvtlo5s666945.node0")
parent_window=driver.current_window_handle
time.sleep(3)
driver.find_element(By.XPATH,"//span[text()='Open']").click()
windowId=driver.window_handles
for s in windowId:
    driver.switch_to.window(s)
    if driver.title.__eq__("Dashboard"):
        window_text=driver.find_element(By.XPATH,"//textarea[@id='message']").send_keys("Suvetha")
        driver.close()
        break
time.sleep(5)
driver.switch_to.window(parent_window)
time.sleep(5)'''


import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
#driver.get("https://www.flipkart.com/")
#driver.find_element(By.XPATH,"(//div[@class='zlQd20 _1eDlvI'])[1]").click()
driver.get("https://www.flipkart.com/tyy/4io/~cs-qmhvm2xfhp/pr?sid=tyy%2C4io&collection-tab-name=Vivo+T3X+5G&param=2792&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InZhbHVlQ2FsbG91dCI6eyJtdWx0aVZhbHVlZEF0dHJpYnV0ZSI6eyJrZXkiOiJ2YWx1ZUNhbGxvdXQiLCJpbmZlcmVuY2VUeXBlIjoiVkFMVUVfQ0FMTE9VVCIsInZhbHVlcyI6WyJGcm9tIOKCuTEyLDQ5OSoiXSwidmFsdWVUeXBlIjoiTVVMVElfVkFMVUVEIn19LCJ0aXRsZSI6eyJtdWx0aVZhbHVlZEF0dHJpYnV0ZSI6eyJrZXkiOiJ0aXRsZSIsImluZmVyZW5jZVR5cGUiOiJUSVRMRSIsInZhbHVlcyI6WyJWaXZvIFQzWCA1RyJdLCJ2YWx1ZVR5cGUiOiJNVUxUSV9WQUxVRUQifX0sImhlcm9QaWQiOnsic2luZ2xlVmFsdWVBdHRyaWJ1dGUiOnsia2V5IjoiaGVyb1BpZCIsImluZmVyZW5jZVR5cGUiOiJQSUQiLCJ2YWx1ZSI6Ik1PQkdaUk5FUktEVjVFQ0YiLCJ2YWx1ZVR5cGUiOiJTSU5HTEVfVkFMVUVEIn19fX19")
parent_window=driver.current_window_handle
time.sleep(3)
page_title=driver.title
print(page_title)
windowId=driver.window_handles
for s in windowId:
    driver.switch_to.window(s)
    if driver.title.__eq__(page_title):
        window_text=driver.find_element(By.XPATH,"(//div[@class='_4WELSP'])[1]").click()
        break
time.sleep(5)
driver.switch_to.window(parent_window)
time.sleep(5)



