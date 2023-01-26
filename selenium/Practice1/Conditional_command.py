from selenium import webdriver
import time
driver=webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://masterprograming.com/contact-us/")
print(driver.title)
driver.maximize_window()

time.sleep(20)
var=driver.find_element_by_class_name("search-field")
print(var.is_displayed())

var1=driver.find_element_by_name("s")
print(var1.is_enabled())

# var2=driver.find_element_by_class_name("serach-field")
# print(var2.is_selected())

driver.close()
