*** Settings ***
Library           SeleniumLibrary


*** Variables ***
${browser}  chrome
${url}  https://opensource-demo.orangehrmlive.com/web/index.php/auth/login

*** Test Cases ***
LoginTest
    # Create Webdriver    chrome    executable_path="C:\work\chromedriver.exe"
    open browser    ${url}  ${browser}
    maximize browser window
    sleep   3
    input text  name:username   Admin
    sleep   3
    input text  name:password   admin123
    click element    xpath://button[@type='submit']

ListBox
    open browser    ${url}  ${browser}
    maximize browser window
    sleep   3
    input text  name:username   Admin
    sleep   3
    input text  name:password   admin123
    click element    xpath://button[@type='submit']



*** Keywords ***




