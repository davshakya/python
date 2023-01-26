from selenium import webdriver
import time


driver=webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://www.bing.com/")
driver.find_element_by_id("sb_form_q").send_keys("Devendra Shakya")   
driver.find_element_by_xpath("//label[@for='sb_form_go']").click()
time.sleep(5)
driver.quit()
