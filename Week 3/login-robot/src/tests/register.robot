*** Settings ***
Resource  resource.robot

*** Test Cases ***
Register With Valid Username And Password
    Input New Command
    Input Credentials  emma  emma1234
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input New Command
    Input Credentials  emma  emma1234
    Input New Command
    Input Credentials  emma  emma1234
    Output should Contain  User with username emma already exists

Register With Too Short Username And Valid Password
    Input New Command
    Input Credentials  e  emma1234
    Output should Contain  Username must only contain letters a-z and be at least 3 characters long

Register With Valid Username And Too Short Password
    Input New Command
    Input Credentials  emma  emma1
    Output should Contain  Password must be at least 8 characters long and contain at least 1 number

Register With Valid Username And Long Enough Password Containing Only Letters
    Input New Command
    Input Credentials  emma  emmaemma
    Output should Contain  Password must be at least 8 characters long and contain at least 1 number