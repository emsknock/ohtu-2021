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

*** Keywords ***
Set Registration
    [Arguments]  ${username}  ${password}
    Input text  username  ${username}
    Input password  password  ${password}
    Input Password  password_confirmation  ${password}

Submit Credentials
    Click Button  Register