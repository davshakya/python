*** Settings ***
Library    RequestsLibrary
Library    Collections
Library    String

*** Variables ***
${base_url}    =     https://reqres.in

*** Test Cases ***
TC_Getting_userInfo
    create session    myssion    ${base_url}
    ${endpoint}     set variable    /api/users?page=1
    ${response}=    GET On Session    myssion    ${endpoint}
    Log To Console  ${response.content}
#    Log To Console  ${response.content}
#    Log To Console  ${response.headers}

