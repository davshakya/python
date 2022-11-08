*** Settings ***
Library           SeleniumLibrary


*** Variables ***
${browser}  chrome
${url}  https://opensource-demo.orangehrmlive.com/web/index.php/auth/login

*** Test Cases ***

ListBox
    open browser    ${url}  ${browser}
    maximize browser window
    sleep   1
    input text  name:username   Admin
    sleep   1
    input text  name:password   admin123
    click element    xpath://button[@type='submit']
    select from list by label    oxd-icon bi-caret-down-fill oxd-select-text--arrow  Freelance
#    select from list by index       Employment Status 3

*** Keywords ***




