*** Settings ***
Library    DatabaseLibrary
Library    OperatingSystem
Suite Setup    Connect To Database    pymysql    ${DBName}    ${DbUser}    ${DBPass}     ${DBHost}    ${DBPort}       
Suite Teardown    Disconnect From Database 

*** Variables ***
${DBName}    world
${DbUser}    root
${DBPass}    tiger
${DBHost}    localhost
${DBPort}    3306


*** Test Cases ***
Create person table
    Execute Sql String    Create table school(id int, first_name  varchar(20), last_name varchar(20))
