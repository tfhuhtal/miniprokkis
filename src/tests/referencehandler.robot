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
    Input    1--5
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

Pages Field Must Be In Right Format
    Input    1
    Input    aff
    Input    book
    Input    foo
    Input    bar
    Input    Koira
    Input    2002
    Input    ${EMPTY}
    Input    ${EMPTY}
    Input    1, 1-5
    Input    exit
    Run and Quit
    Output Should Contain    pages

Year Field Must Be In Right Format
    Input    1
    Input    fff
    Input    book
    Input    foo
    Input    bar
    Input    Koira
    Input    02
    Input    exit
    Run and Quit
    Output Should Contain    year

*** Keywords ***
Run And Quit
    Input    0
    Run Application