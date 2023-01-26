from selenium import webdriver

driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("HTTP://google.com/")
driver.maximize_window()
print(driver.title)
driver.close()
