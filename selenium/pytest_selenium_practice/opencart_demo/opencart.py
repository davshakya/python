import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome(executable_path="C:\work\chromedriver.exe")
driver.get("http://localhost/opencart/upload/")
driver.maximize_window()
driver.find_element(By.XPATH, "//span[normalize-space()='My Account']").click()
driver.find_element(By.XPATH, "//a[normalize-space()='Register']").click()
driver.find_element(By.XPATH, "//input[@id='input-firstname']").send_keys("Manan")
driver.find_element(By.XPATH, "//input[@id='input-lastname']").send_keys("Shakya")
driver.find_element(By.XPATH, "//input[@id='input-email']").send_keys("manan@gmail.com")
driver.find_element(By.XPATH, "//input[@id='input-password']").send_keys("manan123")
WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, "//input[@id='input-newsletter-yes']")))
driver.find_element(By.XPATH, "//input[@id='input-newsletter-yes']").click()
driver.find_element(By.XPATH, "//input[@name='agree']").click()
driver.find_element(By.XPATH, "//button[@type='submit']").click()

time.sleep(4)
driver.close()
