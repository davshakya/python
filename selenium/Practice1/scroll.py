from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import time

driver = webdriver.Chrome(executable_path="C:\work\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
# driver.execute_script("window.scrollTo(0, 2000)")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)
driver.execute_script("window.scrollTo(0, -2000)")
time.sleep(5)
driver.close()