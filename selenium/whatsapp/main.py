from selenium import webdriver
driver=webdriver.Chrome(executable_path="C:\\work\\chromedriver.exe")
driver.get("https://web.whatsapp.com/")
driver.implicitly_wait(120)
rj=driver.find_element_by_xpath("//*[@id='pane-side']/div/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span")
rj.click()
driver.implicitly_wait(3)
driver.close()

