*** Settings ***
Library    RequestsLibrary
Library    Collections

*** Variables ***
${base_url}    =     https://reqres.in


*** Test Cases ***
TC_for_postmethod
    Create Session    mysession     ${base_url}
    ${endpoint}     Set Variable    /api/users
    ${body}     Create Dictionary    name=sankar job=QA Engineer
    ${response}=    POST On Session    mysession    ${endpoint}     data=${body}
    log To Console  ${response.status_code}
    log To Console  ${response.contents}


    #Validiation
    ${status_code}=     convert to string   ${response.status_code}
    Should Be Equal     ${response.status_code} 201