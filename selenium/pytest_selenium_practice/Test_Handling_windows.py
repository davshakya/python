import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# tab1 = driver.window_handles[0]
driver.maximize_window()
time.sleep(5)
driver.find_element(By.XPATH, "//a[@id='opentab']").click()
# tab1 = driver.window_handles[1]
time.sleep(5)
for i in range(2):
    driver.switch_to.window(driver.window_handles[i])
    try:
        check_element = driver.find_element(By.XPATH, "//a[@class='btn btn-theme btn-sm btn-min-block']").is_displayed()
        print(check_element)
        if check_element:
            print("Element found in window => ",i)
            driver.close()
        else:
            print("Element not found")
    except:
        print("It is wrong window => ",i)
time.sleep(2)
driver.quit()

