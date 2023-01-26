import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service('chromedriver.exe')
driver = webdriver.Chrome(service=s)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

driver.find_element(By.XPATH,"")
time.sleep(5)
driver.close()
