'''import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
#to get complete table
tables=driver.find_elements(By.XPATH,"//table[@id='table1']")
for data in tables:
    print(data.text)
#have the single heading
tables1=driver.find_elements(By.XPATH,"//table[@id='table1']//th")
for data1 in tables1:
    print(data1.text)
#to get all the heading
tables2=driver.find_elements(By.XPATH,"//table[@id='table1']//thead")
for data2 in tables2:
    print(data2.text)
#to get body
tables3=driver.find_elements(By.XPATH,"//table[@id='table1']//tbody")
for data3 in tables3:
    print(data3.text)
#to get elements in the body
tables4=driver.find_elements(By.XPATH,"//table[@id='table1']//td")
for data4 in tables4:
    print(data4.text)
#to have individual elements
tables5=driver.find_elements(By.XPATH,"//table[@id='table1']/tbody/tr/td")
for data5 in tables5:
    print(data5.text)
#to have the 1st row elements
tables=driver.find_elements(By.XPATH,"//table[@id='table1']/tbody/tr[1]")
for data in tables:
    print(data.text)
#to have in the column
tables1=driver.find_elements(By.XPATH,"//table[@id='table1']/tbody/tr[1]/td")
for data1 in tables1:
    print(data1.text)
#to have 1st row 1st element
tables2=driver.find_elements(By.XPATH,"//table[@id='table1']/tbody/tr[1]/td[1]")
for data2 in tables2:
    print(data2.text)
#to have 1st column values
tables3=driver.find_elements(By.XPATH,"//table[@id='table1']//tr/td[1]")
for data3 in tables3:
    print(data3.text)
#to get particular elements by index
tables4=driver.find_elements(By.XPATH,"//table[@id='table1']//tr[2]/td[3]")
for data4 in tables4:
    print(data4.text)
#to have entire column
tables5=driver.find_elements(By.XPATH,"//table[@id='table1']//tr/td[3]")
for data5 in tables5:
    print(data5.text)
#to find number of rows
tables1 = driver.find_elements(By.XPATH, "//table[@id='table1']//tr")
# Printing row data
for data1 in tables1:
    print(data1.text)

# Finding and printing row count
row_count = len(tables1)
print(row_count)
tables2 = driver.find_elements(By.XPATH, "//table[@id='table1']//th")
column_count = len(tables2)
print(column_count)
for r in range(1, row_count + 1):
    for c in range(1, column_count + 1):
        if r == 1:
            data2 = driver.find_element(By.XPATH, "//table[@id='table1']//tr[" + str(r) + "]//th[" + str(c) + "]")
            print(data2.text, end=' ')
        else:
            data3 = driver.find_element(By.XPATH, "//table[@id='table1']//tr[" + str(r-1) + "]//td[" + str(c) + "]")
            print(data3.text, end=' ')
    print()'''

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://thinking-tester-contact-list.herokuapp.com/")
driver.find_element(By.ID,value="email").send_keys("suvethajayagopi@gmail.com")
driver.find_element(By.ID,"password").send_keys("Suvetha@13")
driver.find_element(By.ID, "submit").click()
time.sleep(5)
'''tables1=driver.find_elements(By.XPATH,"//table[@id='myTable']//th")
for data1 in tables1:
    print(data1.text)'''
suvetha_record=driver.find_elements(By.XPATH,"//table[@id='myTable']//tr[4]")
for data2 in suvetha_record:
    print(data2.text)
excepted_name="Kumara P"
name=driver.find_elements(By.XPATH,value="//table[@id='myTable']//tr/td[2]")
count=len(name)
print(count)
for contact in name:
    print(contact.text)
i=1
for contact in name:
    if contact.text.__eq__(excepted_name):
        actual_data=driver.find_elements(By.XPATH,value="//table[@id='myTable']/tr["+str(i)+"]")
        for actname in actual_data:
            print(actname.text)
    i=i+1
time.sleep(5)








