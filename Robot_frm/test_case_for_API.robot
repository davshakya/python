*** Settings ***
Library    RequestsLibrary


*** Variables ***
${base_url}    =     https://reqres.in
${user_iD} =    1


*** Test Cases ***
Test_to_get_userInfo
    create session    myssion    ${base_url}   
    ${response}=    get Request    myssion    /api/users/${user_iD} 
    log to console ${response.status_code}    
    log to console ${response.content}    
    log to console ${response.headers}    
    
 