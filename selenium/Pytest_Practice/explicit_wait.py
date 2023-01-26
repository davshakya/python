from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome(executable_path="C:\work\chromedriver.exe")
driver.get("https://chercher.tech/practice/implicit-wait-example")
driver.maximize_window()

WebDriverWait(driver,15).until(expected_conditions.element_to_be_clickable((By.XPATH,"//body/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/input[1]")))
driver.find_element_by_xpath("//body/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/input[1]").click()


# driver.implicitly_wait(5)
driver.close()




