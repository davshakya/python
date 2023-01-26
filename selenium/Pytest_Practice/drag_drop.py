from selenium import webdriver
from selenium.webdriver import  ActionChains
driver=webdriver.Chrome(executable_path="C:\work\chromedriver.exe")
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()

src=driver.find_element_by_xpath("//div[@id='box101']")
dest=driver.find_element_by_xpath("//*[@id='box101']")
action=ActionChains(driver)
action.move_to_element(src,dest).perform()