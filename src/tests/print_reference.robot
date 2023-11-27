*** Settings ***
Resource    resource.robot

*** Test Cases ***
List References
    Input    2
    Input    0
    Run Application
    Output Should Contain    Viitelista

List References In Bibtext
    Input    4
    Input    0
    Run Application
    Output Should Contain    bibtex

Remove Reference That Does Not Exist
    Input  3
    Input  olematonavain
    Input  ${EMPTY}
    Input  0
    Run Application
    Output Should Contain  Tarkista

*** Keywords ***
