import time
from selenium import webdriver
driver=webdriver.Chrome(executable_path="C:\work\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
# driver.find_element_by_id("exampleFormControlSelect1").click()
driver.find_element_by_xpath("//option[contains(text(),'Male')]").click()
dropdown=Select()
time.sleep(5)
driver.close()


