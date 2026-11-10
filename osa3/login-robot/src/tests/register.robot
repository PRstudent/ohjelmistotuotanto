*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command


*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  johnny  johnny123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  al  alexander123
    Output Should Contain  Username is too short

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  5imon  5imon123
    Output Should Contain  Username can only have lower case characters a-z

Register With Valid Username And Too Short Password
    Input Credentials  alexander  al123
    Output Should Contain  Password is too short (under 8 characters)

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  ferdinand  Ferdinand
    Output Should Contain  Password cannot be formed only from letters


*** Keywords ***
Create User And Input New Command
    Create User  kalle  kalle123
    Input New Command
