from selenium import webdriver
import time
driver=webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("HTTP://masterprograming.com/")
driver.maximize_window()
print(driver.title)
time.sleep(5)
driver.get("HTTP://google.com/")
print(driver.title)
driver.back()
time.sleep(5)
driver.forward()

driver.close()  


