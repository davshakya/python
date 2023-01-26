from selenium import webdriver
import time
from selenium.webdriver import ActionChains


from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome(executable_path="chromedriver.exe")
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.get("https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver")

driver.maximize_window()
print(driver.title)
print(driver.current_url)
# driver.find_element_by_xpath("//*[@id='autocomplete']").send_keys("Devendra")
# time.sleep(2)
# driver.find_element_by_id("openwindow").click()
# driver.find_element_by_xpath("//select[@id='dropdown-class-example']/option[2]").click()

# action=ActionChains(driver)
# action.move_to_element(driver.find_element_by_xpath("//button[@id='mousehover']")).perform()
# action.move_to_element(driver.find_element_by_xpath("/html/body/div[4]/div/fieldset/div/div/a[1]")).click().perform()

driver.find_element_by_xpath("//button[@id='populate-text']").click()   
WebDriverWait(driver,12).until(expected_conditions.text_to_be_present_in_element((By.XPATH,"//h2[@id='h2']"),"Selenium Webdriver"))
print(driver.find_element_by_xpath("//h2[@id='h2']").text)                              
driver.save_screenshot('s.png')
driver.execute_script("window.scrollTo(0, 200)") 
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

time.sleep(2)
driver.quit()



