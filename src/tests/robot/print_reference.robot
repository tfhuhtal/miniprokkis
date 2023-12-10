*** Settings ***
Resource    resource.robot

*** Test Cases ***
Käyttäjä Voi Tulostaa Viitelistan Konsoliin
    Input    2
    Input    0
    Run Application
    Output Should Contain    Viitelista

Käyttäjä Voi Tulostaa Lähdeviitteitä Aakkosjärjestyksessä
    Input    2 -a
    Run And Quit
    Output Should Contain    aakkosjärjestyksessä

Käyttäjä Voi Tulostaa Lähdeviitteitä Tiiviissä Muodossa
    Input    2 -c
    Run And Quit
    Output Should Contain    Tiiviissä

Käyttäjä Voi Tulostaa Lähdeviitteitä Aakkosjärjestyksessä Tiiviissä Muodossa 
    Input    2 -c -a
    Run And Quit
    Output Should Contain    Tiiviissä
    Output Should Contain    aakkosjärjestyksessä

Käyttäjä Voi Tulostaa Viitelistan Konsoliin Bibtext-muodossa
    Input    4
    Input    0
    Run Application
    Output Should Contain    bibtex

Käyttäjä Voi Tulostaa Lähteet Bibtxt-muodossa Erilliseen Tiedstoon
    Input    4 -f
    Input    testi
    Run And Quit
    Output Should Contain    bib


*** Keywords ***
Run And Quit
    Input    0
    Run Application

Delete Reference
    Input    3
    Input    Testiavain