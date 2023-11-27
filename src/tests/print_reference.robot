*** Settings ***
Resource  resource.robot

*** Test Cases ***
Print Reference List
    Input  ENTER
    Input  2
    Input  ENTER
    Run App
    Output Should Contain  ""