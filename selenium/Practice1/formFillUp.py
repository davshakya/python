import time
from selenium import webdriver
from selenium.webdriver.support.select import Select


driver=webdriver.Chrome(executable_path="chromedriver.exe")
driver.get('https://www.salesforce.com/in/form/signup/freetrial-sales/?d=70130000000Enyk')  
driver.maximize_window()
obj=driver.find_element_by_name("UserTitle")
# p1=obj.find_elements_by_tag_name("option")
p1=obj.find_elements_by_tag_name("option")

print(len(p1))
for element in range(len(p1)):
    if p1[element].is_displayed():
        print(p1[element].text)
       
driver.close()
 
 
 