import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
import validators
import requests
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# # driver.get("https://the-internet.herokuapp.com/upload")
# driver.get("https://chercher.tech/practice/implicit-wait-example")
# driver.get("https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver")
# driver.get("https://the-internet.herokuapp.com/context_menu")
driver.maximize_window()
# driver.implicitly_wait(10)


# driver.find_element_by_id("name").send_keys("Devendra")
# x = driver.find_element_by_xpath("/html/body/div[2]/div[2]/fieldset/legend").text
# print(x)
# x=driver.find_element_by_xpath("//legend[text()='Suggession Class Example']").text
# print(x)

# print(driver.get_cookies())


# links = driver.find_elements(By.TAG_NAME,"a")
# # img = driver.find_element_by_css_selector(("img"))
# for link in links:
#     url = link.get_attribute("href")
#     print(url)
# if validators.url(url):

#     r = requests.head(url)
#     rs_code = r.status_code
#     # print(url,rs_code)
# else:
#     print("Invalid Links",url)
#
#     if rs_code != 200:
#         print(url, rs_code)


# driver.find_element_by_xpath('//*[@id="checkBoxOption1"]').click()
# driver.find_element_by_css_selector("input[value='radio2']").click()
# driver.find_element_by_xpath("//input[@value='radio1']").click()
# t = driver.find_element_by_xpath("//legend[text()='Checkbox Example']").text


# c=driver.find_elements_by_xpath("//*[contains(@class,'input')]")
# for i in c:
#     print(i.tag_name)
# print(t)

# checbx = driver.find_elements_by_xpath("//div[@class='right-align']/fieldset/label/input")
# for i in checbx:
#     i.click()


select_drop_down = Select(driver.find_element(By.XPATH,"//select[@id='dropdown-class-example']"))
select_drop_down.select_by_value("option1")
time.sleep(2)
select_drop_down.select_by_index(2)
time.sleep(2)
select_drop_down.select_by_visible_text("Option3")

# driver.find_element_by_xpath("//input[@placeholder='Type to Select Countries']").send_keys("ind")
# time.sleep(5)
# from_countries = driver.find_elements_by_xpath("/html[1]/body[1]/ul[1]/li/div")
# for country in from_countries:
#     print(country.text)
#     if country.text=="India":
#         country.click()
#         time.sleep(2)
#         print(country.text)
#     else:
#         pass


# driver.find_element(By.XPATH,"//input[@name='enter-name']").send_keys("Devnedra")
# time.sleep(2)
# driver.find_element(By.XPATH,"//input[@id='alertbtn']").click()
# popup=driver.switch_to.alert
# time.sleep(2)
# print(popup.text)
# popup.dismiss()

# driver.find_element_by_xpath("//input[@id='file-upload']").send_keys("C:\\work\\abc.txt")
# driver.find_element_by_xpath("//input[@id='file-submit']").click()

# driver.implicitly_wait(5)
# driver.find_element_by_xpath("//div[@id='q']/input[1]").click()
# driver.find_element_by_xpath("//div[@id='q']/input[2]").click()

# WebDriverWait(driver,10).until(ec.element_to_be_clickable((By.XPATH,"//div[@id='q']/input[1]")))
# driver.find_element_by_xpath("//div[@id='q']/input[1]").click()
# WebDriverWait(driver,20).until(ec.element_to_be_clickable((By.XPATH,"//div[@id='q']/input[2]")))
# driver.find_element_by_xpath("//div[@id='q']/input[2]").click() 


# try:
#     driver.find_element_by_xpath("//button[@id='populate-text']").click()
#     WebDriverWait(driver,1).until(ec.text_to_be_present_in_element((By.XPATH,"//h2[@class='target-text']"),"Selenium Webdriver"))

# except TimeoutException:
#     print("timeout exception error occured")


# agent = driver.execute_script("return navigator.userAgent")
# print(agent)
# # directly print the value
# print(driver.execute_script("return navigator.userAgent"))


# action=ActionChains(driver)
# action.move_to_element(driver.find_element_by_xpath("//button[@id='mousehover']")).perform()
# time.sleep(2)
# action.move_to_element(driver.find_element_by_xpath("//a[@href='#top']")).click().perform()


# action=ActionChains(driver)
# action.context_click(driver.find_element_by_xpath("//div[@id='hot-spot']")).perform()


# driver.find_element_by_xpath("//a[@id='opentab']").click()
# tab=driver.window_handles[1]
# driver.find_element_by_xpath("//button[@id='openwindow']").click()
# print(driver.window_handles)
# wind2=driver.window_handles[2]
# driver.switch_to_window(driver.window_handles[1])
# driver.find_element_by_xpath("//div[@class='nav-outer clearfix']//a[normalize-space()='Courses']").click()
# driver.switch_to_window(driver.window_handles[2])
# driver.find_element_by_xpath("//*[@id='homepage']/header/div[2]/div/nav/ul/li[5]/a").click()


# frame=driver.find_element_by_xpath("//iframe[@id='courses-iframe']")
# time.sleep(5)
# driver.switch_to.frame(frame)
# driver.find_element_by_xpath("//a[@href='consulting']").click()
# time.sleep(5)
# driver.switch_to_default_content()
# driver.find_element_by_xpath("//*[@id='name']").send_keys("Devendra")


# x=driver.find_element_by_xpath("//*[@id='name']").get_attribute("placeholder")
# driver.find_element_by_xpath("//*[@id='name']").send_keys("Devendra")
# x=driver.find_element_by_xpath("//*[@id='name']").get_attribute("value")
# print(x)

# driver.execute_script("window.scrollTo(0,1500)")
# driver.save_screenshot("sss.png")

# driver.execute_script("document.body.style.zoom='150%'")
# time.sleep(1)
# driver.execute_script("document.body.style.zoom='50%'")
# time.sleep(1)
# driver.execute_script("document.body.style.zoom='100%'")


print(driver.title)
print(driver.current_url)
time.sleep(2)
driver.quit()
