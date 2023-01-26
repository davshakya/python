from selenium import webdriver
class Testlogin:
    def test_login():
        driver=webdriver.Chrome(executable_path="C:\\work\\chromedriver.exe")
        driver.get("https://opensource-demo.orangehrmlive.com/index.php/dashboard")
        driver.maximize_window()
        driver.find_element_by_xpath("//input[@id='txtUsername']").send_keys("Admin")  
        driver.find_element_by_xpath("//form[@id='frmLogin']").send_keys("admin123")
        driver.find_element_by_xpath("//input[@id='txtUsername']").click()  
        driver.close()
Testlogin.test_login()      