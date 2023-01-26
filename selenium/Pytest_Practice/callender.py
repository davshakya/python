from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\work\chromedriver.exe")
driver.get("http://seleniumpractise.blogspot.com/2016/08/how-to-handle-calendar-in-selenium.html")
driver.maximize_window()
driver.find_element(By.ID,"datepicker").click()
driver.implicitly_wait(5)
date=driver.find_elements_by_xpath("//tbody/tr/td/a")
driver.implicitly_wait(5)
for i in date:
    if i.text=="25":
        i.click()
    else:
        pass
driver.close()