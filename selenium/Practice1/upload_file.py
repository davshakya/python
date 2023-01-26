from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get('https://the-internet.herokuapp.com/upload')

driver.maximize_window()
driver.find_element_by_xpath("//input[@id='file-upload']").send_keys("F:\\test1.jpg")
driver.find_element_by_xpath("//input[@id='file-submit']").click()