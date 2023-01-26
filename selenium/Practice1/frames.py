from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(30)

driver.switch_to_frame(driver.find_element_by_xpath("//ul[@class='clearfix']"))
driver.find_element_by_xpath("//div[@class='nav-outer clearfix']//a[normalize-space()='Job Support']").click()
driver.switch_to_default_content()
time.sleep(2)
driver.quit()









