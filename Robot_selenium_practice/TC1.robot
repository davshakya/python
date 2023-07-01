*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${browser}  chrome
${url}  https://rahulshettyacademy.com/AutomationPractice/
${radio}        //*[contains(text(),'Option4')]

*** Test Cases ***
LoginTest
    Create Webdriver    chrome        executable_path="C:\work\chromedriver.exe"
    OPEN BROWSER    ${url}      ${browser}
    maximize browser window
    set selenium speed  3
    LoginToApplication
    click element    xpath://input[@value='radio1']
    ${isExist}=  Run Keyword And Return Status    Element Should Be Visible    ${radio}
    Log To Console    ${isExist}
    close browser


*** Keywords ***
LoginToApplication
    click element    xpath://input[@id='checkBoxOption1']
    input text  xpath://input[@id='name']   Devendra

    select checkbox  checkBoxOption2
#    sleep  3
    select from list by label  dropdown-class-example   Option1
#    sleep   3
    select from list by index  dropdown-class-example   3
