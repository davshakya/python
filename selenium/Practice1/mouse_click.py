from selenium import webdriver
import time
from selenium.webdriver import  ActionChains
driver = webdriver.Chrome(executable_path="C:/Users/davsh/My Drive/Computer_Programmes/chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/context_menu")
action=ActionChains(driver)
action.context_click(driver.find_element_by_xpath("//div[@id='hot-spot']")).perform()
action.double_click(driver.find_element_by_xpath("//div[@id='hot-spot']")).perform()

time.sleep(2)
driver.close()




