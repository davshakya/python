import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
import validators
import requests
from webdriver_manager.chrome import ChromeDriverManager


def Test_HandingW():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # driver=webdriver.Chrome(executable_path="chromedriver.exe")
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    tab1 = driver.window_handles[0]
    time.sleep(5)
    driver.find_element(By.XPATH, "//a[@id='opentab']").click()
    tab1 = driver.window_handles[1]
    time.sleep(5)
    # driver.find_element(By.XPATH, "//a[@id='opentab']").click()
    # tab2 = driver.window_handles[2]
    for i in range(2):
        driver.switch_to.window(driver.window_handles[i])
        check_element = driver.find_element(By.XPATH, "//a[@class='btn btn-theme btn-sm btn-min-block']").is_displayed()
        if check_element:
            print("Element found")
        else:
            print("Element not found")


    # driver.find_element(By.XPATH, "//button[@id='openwindow']").click()
    # print(driver.window_handles)
    # wind2 = driver.window_handles[2]
    # driver.switch_to.window(driver.window_handles[1])
    # driver.find_element(By.XPATH, "//div[@class='nav-outer clearfix']//a[normalize-space()='Courses']").click()
    # driver.switch_to.window(driver.window_handles[2])
    # driver.find_element(By.XPATH, "//*[@id='homepage']/header/div[2]/div/nav/ul/li[5]/a").click()

    print(driver.title)
    print(driver.current_url)
    time.sleep(2)
    # driver.quit()
