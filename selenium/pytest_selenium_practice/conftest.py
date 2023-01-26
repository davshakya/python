import pytest
from selenium import webdriver

@pytest.fixture(scope="module")
def setup():
    print("It will run first")
    # driver = webdriver.Chrome(executable_path="C:\work\chromedriver.exe")
    # driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    # driver.maximize_window()
    yield
    print("It will run at the end")
    # driver.quit()
