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

Käyttäjä Voi Hakea Lähdeviitteitä Hakusanalla
    Lisää Testi Lähdeviite
    Input    5
    Input    Testi
    Poista Testi Lähdeviite
    Run And Quit
    Output Should Contain    TestiTitle

Käyttäjä Voi Hakea Lähdeviitteitä Hakusanalla Kompaktina Tulosteena
    Lisää Testi Lähdeviite
    Input    5 -c
    Input    Testi
    Poista Testi Lähdeviite
    Run And Quit
    Output Should Contain    TestiTitle

Käyttäjä Voi Hakea Lähdeviitteitä Avaimella
    Lisää Testi Lähdeviite
    Input    6
    Input    Testiavain
    Poista Testi Lähdeviite
    Run And Quit
    Output Should Contain    TestiTitle

Käyttäjä Voi Hakea Lähdeviitteitä Avaimella Kompaktina Tulosteena
    Lisää Testi Lähdeviite
    Input    6
    Input    Testiavain
    Poista Testi Lähdeviite
    Run And Quit
    Output Should Contain    TestiTitle

Käyttäjä voi tallentaa lähdetiedot ulkoiseen tiedostoon ja nimetä tiedostoon
    Input    4 -f
    Input    testi
    Run And Quit
    Output Should Contain    testi


*** Keywords ***
Run And Quit
    Input    0
    Run Application

Poista Testi Lähdeviite
    Input    3
    Input    Testiavain

Lisää Testi Lähdeviite
    Input    1
    Input    Testiavain
    Input    2
    Input    TestiAuthor
    Input    TestiTitle
    Input    TestiPublisher
    Input    2002
    Input    ${EMPTY}
    Input    ${EMPTY}
    Input    ${EMPTY}
    Input    ${EMPTY}
    Input    ${EMPTY}
    Input    ${EMPTY}