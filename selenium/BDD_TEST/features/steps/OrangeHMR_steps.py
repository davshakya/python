from behave import *
from selenium import webdriver


@given('launch chrome browser')
def launch_chrome(context):
    context.driver = webdriver.Chrome(executable_path="F:\Computer_Programmes\chromedriver.exe")
    # context.driver=webdriver.Chrome()

@when('Open OrangeHRM homepage')
def open_homepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")

@then('verify that the Logo present on homepage')
def verify_logo(context):
    status = context.driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/img").is_displayed()
    assert status is True


@then('close browser')
def close_browser(context):
    context.driver.close()


# Note########
'''To execute test cases & generate report files( .json).
--------------------------------------------------
 behave -f allure_behave.formatter:AllureFormatter -o reports/ features

To Generate Allure report
--------------------------------------------
allure serve reports'''


