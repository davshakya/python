import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="chromedriver.exe")
driver.get('https://wwww.bing.com')  
driver.maximize_window()
p1=driver.find_elements_by_tag_name("a")
for element in range(len(p1)):
    if p1[element].is_displayed():
        print(p1[element].text)
        p1[element].send_keys(Keys.TAB)
time.sleep(2)
driver.quit()


 
 
 