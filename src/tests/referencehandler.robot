*** Settings ***
Resource  resource.robot

*** Test Cases ***
Add Reference
    Input    1
    Input    sdf
    Input    book
    Input    foo
    Input    bar
    Input    Koira
    Input    2002
    Input    ${EMPTY}
    Input    ${EMPTY}
    Input    ${EMPTY}
    Input    ${EMPTY}
    Input    ${EMPTY}
    Input    ${EMPTY}
    Run and Quit
    Output Should Contain    lisätty

Delete Reference
    Input    3
    Input    sdf
    Run And Quit
    Output Should Contain    poistettu

*** Keywords ***
Run And Quit
    Input    0
    Run Application