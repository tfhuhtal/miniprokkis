*** Settings ***
Resource    resource.robot

*** Test Cases ***
AddReferenceAndList
    Input    2
    Input    0
    Run Application
    Output Should Contain    Viitelista  
*** Keywords ***
