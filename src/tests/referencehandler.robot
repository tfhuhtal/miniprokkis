*** Settings ***
Resource  resource.robot

*** Test Cases ***
Käyttäjä Voi Lisätä Kirja Viitteen
    Input    1
    Input    Testiavain
    Input    2
    Input    Auth
    Input    Titl
    Input    Publ
    Input    2002
    Input    Vol
    Input    Numb
    Input    1--5
    Input    Mth
    Input    Note
    Input    Isbn
    Run and Quit
    Output Should Contain    lisätty

Käyttäjä Voi Postaa Viitteen
    Input    3
    Input    Testiavain
    Run And Quit
    Output Should Contain    poistettu

Käyttäjä Voi Lisätä Artikkeli Viitteen
    Input    1
    Input    Testiavain
    Input    1
    Input    Auth
    Input    Titl
    Input    Publ
    Input    2002
    Input    Vol
    Input    Numb
    Input    1--5
    Input    Mth
    Input    Note
    Input    Isbn
    Delete Reference
    Run and Quit
    Output Should Contain    lisätty

Käyttäjä Voi Lisätä Booklet Viitteen
    Input    1
    Input    Testiavain
    Input    3
    Input    Titl
    Input    Auth
    Input    HowPubl
    Input    2002
    Input    Editor
    Input    Volume
    Input    Number
    Input    series
    Input    Org
    Input    Mnth
    Input    Note
    Delete Reference
    Run and Quit
    Output Should Contain    lisätty

Pages Field Must Be In Right Format
    Input    1
    Input    aff
    Input    2
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
    Input    2
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

Delete Reference
    Input    3
    Input    Testiavain