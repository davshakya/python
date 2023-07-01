*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://rahulshettyacademy.com/AutomationPractice/

*** Keywords ***
Open Chrome Browser
    Open Browser    ${url}    Chrome
    Maximize Browser Window