from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element_by_xpath("//a[@id='opentab']").click()
tab=driver.window_handles[1]
driver.find_element_by_xpath("//button[@id='openwindow']").click()
window2=driver.window_handles[2]
driver.switch_to_window(tab)
# driver.switch_to_window(driver.window_handles[1])
driver.find_element_by_xpath("//div[@class='nav-outer clearfix']//a[normalize-space()='Practice']").click()
driver.switch_to_window(window2)
driver.find_element_by_xpath("//a[normalize-space()='Practice']").click()

time.sleep(2)
driver.quit()




