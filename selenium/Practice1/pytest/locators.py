from selenium import webdriver
import time

from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
driver.maximize_window()
# print(driver.title)
# driver.find_element_by_id("name").send_keys("Devendra Shakya")
# driver.find_element_by_id("alertbtn").click()
# a = driver.find_element_by_id("openwindow").text
# print(a)
# driver.find_element_by_css_selector("input[value='radio1']").click()
# driver.find_element_by_xpath("//input[@value='radio1']").click()
# driver.find_element_by_xpath("//select[@id='dropdown-class-example']/option[2]").click()
# driver.find_element_by_xpath("//select[@id='dropdown-class-example']/option[last()]").click()
# driver.find_element_by_xpath("//div[@class='cen-right-align']/fieldset/select/option[2]").click()

# checkboxes=driver.find_elements_by_xpath("//input[@type='checkbox']")
# print(len(checkboxes))
# for checkbox in checkboxes:
#     print(checkbox)
#     if checkbox == checkboxes[1]:
#         continue
#     else:
#         checkbox.click()

# static_dropdown=Select(driver.find_element_by_xpath("//select[@id='dropdown-class-example']"))
# static_dropdown.select_by_visible_text("Option3")
# time.sleep(1)
# static_dropdown.select_by_index(2)
# time.sleep(1)
# static_dropdown.select_by_value("option1")

# driver.find_element_by_xpath("//input[@id='autocomplete']").send_keys("ind")
# time.sleep(2)
# countries=driver.find_elements_by_xpath("//ul[@id='ui-id-1']/li/div")
# for cnt in countries:
#     print(cnt)
#     if cnt.txt == "India":
#         cnt.click()
#     else:
#         pass

driver.find_element_by_xpath("//input[@id='name']").send_keys("Devendra")
driver.find_element_by_xpath("//input[@id='alertbtn']").click()
popups=driver.switch_to_alert
time.sleep(2)
popups.accept()
print(popups.text)
time.sleep(1)
driver.close()



