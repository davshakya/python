
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import time

driver = webdriver.Chrome(executable_path="C:\work\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
d=driver.find_element(By.XPATH,"//input[@type='checkbox']")
for i in d:
    print(i)
driver.close()



