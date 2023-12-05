*** Settings ***
Resource  resource.robot

*** Test Cases ***
Käyttäjä voi tulostaa lähteet bibtxt-muodossa erilliseen tiedstoon
    Input    4 -f
    Run And Quit
    Output Should Contain    bib

Käyttäjä voi tulostaa lähdeviitteitä tiiviissä muodossa
    Input    2 -c
    Run And Quit
    Output Should Contain    Tiivis

Käyttäjä voi syöttää lähdetyypin valinnan lyhyessä muodossa
    Input    1
    Input    Testiavain
    Input    2
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
    Delete Reference
    Run and Quit
    Output Should Contain    lisätty


*** Keywords ***
Run And Quit
    Input    0
    Run Application

Delete Reference
    Input    3
    Input    Testiavain