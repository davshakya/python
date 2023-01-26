from selenium import webdriver
from selenium.webdriver.common.by import By

print(type(webdriver))
driver = webdriver.Chrome(executable_path="C:\work\chromedriver.exe")

driver.get("https://www.google.com/")
t = driver.title
print(t)
"Google" == t, "Title is wrong"

driver.save_screenshot("sss.png")
x = driver.find_elements(By.TAG_NAME, "a")
print(x)
for i in x:
    print(i.get_attribute("href"))

driver.close()
