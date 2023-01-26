from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

opt = Options()
opt.add_experimental_option("debuggerAddress", "localhost:8989")
driver = webdriver.Chrome(executable_path="C:\work\chromedriver.exe", chrome_options=opt)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.XPATH, "//input[@name='enter-name']").send_keys("Devendra Shakya")
driver.find_element(By.XPATH, '//*[@id="checkBoxOption1"]').click()
driver.find_element(By.CLASS_NAME, "input[value='radio2']").click()
driver.find_element(By.XPATH, "//input[@value='radio1']").click()
t = driver.find_element(By.XPATH, "//legend[text()='Checkbox Example']").text
print(t)
