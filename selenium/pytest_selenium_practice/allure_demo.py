import time
import allure
from selenium import webdriver
import pytest


@pytest.fixture()
def test_setup():
    global driver
    driver=webdriver.Chrome(executable_path="C:\work\chromedriver.exe")
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield    
    driver.quit()

@allure.description("OrangeHRM test with valid credentials")
@allure.severity(severity_level="CRITICAL")
def test_login_valid_input(test_setup):
    driver.find_element_by_xpath("//div[@id='divUsername']/input").send_keys("Admin")
    driver.find_element_by_xpath("//div[@id='divPassword']/input").send_keys("admin123")
    driver.find_element_by_xpath("//input[@type='submit']").click()
    time.sleep(3)
    try:
        assert "dashboard" in driver.current_url
    finally:
        if AssertionError:
            allure.attach(driver.get_screenshot_as_png(),name="allure_demo_invalid_credential",attachment_type=allure.attachment_type.PNG)


@allure.description("OrangeHRM test with invalid credentials")
@allure.severity(severity_level="NORMAL")
def test_login_invalid_input(test_setup):
    driver.find_element_by_xpath("//div[@id='divUsername']/input").send_keys("Admin")
    driver.find_element_by_xpath("//div[@id='divPassword']/input").send_keys("admin1")
    driver.find_element_by_xpath("//input[@type='submit']").click()
    assert "dashboard" in driver.current_url

