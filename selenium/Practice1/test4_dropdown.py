from selenium import webdriver
import time
driver=webdriver.Chrome(executable_path="chromedriver.exe")
driver.get('https://www.bing.com/account/general?ru=https%3a%2f%2fwww.bing.com%2f%3ftoWww%3d1%26redig%3d1E6F5FF0FF114E2699C3C229F80E549C&FORM=O2HV65&id=language_section#language-section')  
driver.maximize_window
driver.find_element_by_id('rpp').send_keys('10')
p1=driver.find_element_by_id('rpp').is_selected()
print(p1)



time.sleep(5)
driver.quit()
