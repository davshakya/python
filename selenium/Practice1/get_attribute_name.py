from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
a=driver.find_element_by_xpath("//input[@id='name']").get_attribute("placeholder")
print(a)
time.sleep(2)
driver.quit()




