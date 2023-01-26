from outcome import acapture
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support.select import select
driver=webdriver.Chrome(executable_path="C:\work\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
g_url="https://rahulshettyacademy.com/AutomationPractice/"
cu=driver.current_url
if g_url==cu:
    print("You are on home page")
driver.maximize_window()
driver.close()


