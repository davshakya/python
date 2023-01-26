from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\work\chromedriver.exe")
driver.get("https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver")
driver.maximize_window()
# WebDriverWait(driver,11).until(expected_conditions.element_to_be_clickable((By.XPATH,"//body/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/input[1]")))
# driver.find_element_by_xpath("//body/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/input[1]").click()
driver.find_element_by_xpath("//button[@id='populate-text']").click()

WebDriverWait(driver, 15).until(
    expected_conditions.text_to_be_present_in_element((By.XPATH, "//h2[@id='h2']"), "Selenium Webdriver"))
print(driver.find_element_by_xpath("//h2[@id='h2']").text)
time.sleep(2)
driver.close()


