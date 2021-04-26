*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Registration  emma  emma1234
    Submit Credentials
    Welcome Page Should Be Open

Register With Too Short Username And Valid Password
    Set Registration  e  emma1234
    Submit Credentials
    Page Should Contain  Username must only contain letters a-z and be at least 3 characters long

*** Keywords ***
Set Registration
    [Arguments]  ${username}  ${password}
    Input text  username  ${username}
    Input password  password  ${password}
    Input Password  password_confirmation  ${password}

Submit Credentials
    Click Button  Register