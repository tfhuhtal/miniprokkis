*** Settings ***
Resource  resource.robot

*** Test Cases ***
Käyttäjä Voi Tulostaa Lähteet Bibtxt-muodossa Erilliseen Tiedstoon
    Input    4 -f
    Input    testi
    Run And Quit
    Output Should Contain    bib

Käyttäjä Voi Tulostaa Lähdeviitteitä Tiiviissä Muodossa
    Input    2 -c
    Run And Quit
    Output Should Contain    Tiiviissä

Käyttäjä Voi Tulostaa Lähdeviitteitä Aakkosjärjestyksessä Tiiviissä Muodossa 
    Input    2 -c -a
    Run And Quit
    Output Should Contain    Tiiviissä
    Output Should Contain    aakkosjärjestyksessä

Käyttäjä Voi Syöttää Lähdetyypin Valinnan Lyhyessä Muodossa
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