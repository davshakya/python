from selenium import webdriver
import time
driver=webdriver.Chrome(executable_path="C:\work\chromedriver.exe")
driver.get("https://www.bing.com/account/general?ru=https%3a%2f%2fwww.bing.com%2f%3ftoWww%3d1%26redig%3d1E6F5FF0FF114E2699C3C229F80E549C&FORM=O2HV65&id=language_section#language-section")  
driver.maximize_window()
# p1=driver.find_element_by_xpath('//*[@id="hpqs_DisableCarousel_ctrl"]').is_selected()
p1=driver.find_element_by_xpath('//*[@id="newwnd"]').is_selected()

print(p1)
if p1==True:
    print("Already Selected")
else:
    # driver.find_element_by_xpath('//*[@id="hpqs_DisableCarousel_ctrl"]').click()
    driver.find_element_by_xpath('//*[@id="newwnd"]').click()
    
    print("Successfully checked")
time.sleep(10)
driver.quit()
