*** Settings ***
Resource  resource.robot

*** Test Cases ***
Käyttäjä Voi Lisätä Kirja Viitteen
    Input    1
    Input    Testiavain
    Input    2
    Input    Author
    Input    Title
    Input    Publisher
    Input    2002
    Input    Volume
    Input    Number
    Input    1--5
    Input    Month
    Input    Note
    Input    Isbn
    Run and Quit
    Output Should Contain    lisätty

Käyttäjä Voi Postaa Viitteen
    Input    3
    Input    Testiavain
    Run And Quit
    Output Should Contain    poistettu

Käyttäjä Voi Jättää Kirjan Vapaaehtoiset Kentät Tyhjiksi
    Input    1
    Input    Testiavain
    Input    2
    Input    Author
    Input    Title
    Input    Publisher
    Input    2002
    Input    ${EMPTY}
    Input    ${EMPTY}
    Input    ${EMPTY}
    Input    ${EMPTY}
    Input    ${EMPTY}
    Input    ${EMPTY}
    Delete Reference
    Run and Quit
    Output Should Contain    lisätty

Käyttäjä Voi Lisätä Artikkeli Viitteen
    Input    1
    Input    Testiavain
    Input    1
    Input    Author
    Input    Title
    Input    Publisher
    Input    2002
    Input    Volume
    Input    Number
    Input    1--5
    Input    Month
    Input    Note
    Input    Isbn
    Delete Reference
    Run and Quit
    Output Should Contain    lisätty

Käyttäjä Voi Jättää Artikkelin Vapaaehtoiset Kentät Tyhjiksi
    Input    1
    Input    Testiavain
    Input    2
    Input    Author
    Input    Title
    Input    Publisher
    Input    2002
    Input    ${EMPTY}
    Input    ${EMPTY}
    Input    ${EMPTY}
    Input    ${EMPTY}
    Input    ${EMPTY}
    Input    ${EMPTY}
    Delete Reference
    Run and Quit
    Output Should Contain    lisätty

Käyttäjä Voi Lisätä Booklet Viitteen
    Input    1
    Input    Testiavain
    Input    3
    Input    Title
    Input    Author
    Input    HowPublished
    Input    2002
    Input    Editor
    Input    Volume
    Input    Number
    Input    series
    Input    Organization
    Input    Month
    Input    Note
    Delete Reference
    Run and Quit
    Output Should Contain    lisätty

Käyttäjä Voi Jättää Booklet Vapaaehtoiset Kentät Tyhjiksi
    Input    1
    Input    Testiavain
    Input    3
    Input    Title
    Input    Author
    Input    HowPublished
    Input    2002
    Input    ${EMPTY}
    Input    ${EMPTY}
    Input    ${EMPTY}
    Input    ${EMPTY}
    Input    ${EMPTY}
    Input    ${EMPTY}
    Input    ${EMPTY}
    Delete Reference
    Run and Quit
    Output Should Contain    lisätty

Käyttäjä Voi Lisätä Inproceedings Viitteen
    Input    1
    Input    Testiavain
    Input    3
    Input    Author
    Input    Title
    Input    booktitle
    Input    2002
    Input    Editor
    Input    Volume
    Input    Number
    Input    series
    Input    1--5
    Input    Month
    Input    Organization
    Input    Publisher
    Input    Note
    Delete Reference
    Run and Quit
    Output Should Contain    lisätty

Käyttäjä Voi Jättää Inproceedings Vapaaehtoiset Kentät Tyhjiksi
    Input    1
    Input    Testiavain
    Input    3
    Input    Author
    Input    Title
    Input    booktitle
    Input    2002
    Input    ${EMPTY}
    Input    ${EMPTY}
    Input    ${EMPTY}
    Input    ${EMPTY}
    Input    ${EMPTY}
    Input    ${EMPTY}
    Input    ${EMPTY}
    Input    ${EMPTY}
    Input    ${EMPTY}
    Delete Reference
    Run and Quit
    Output Should Contain    lisätty

Käyttäjä ei pysty tallentamaan pages-kenttää jos se ei ole oikeaa muotoa
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
    Input    Q
    Run and Quit
    Output Should Contain    pages

Käyttäjä ei pysty tallentamaan vuosilukua tekstimuodossa
    Input    1
    Input    fff
    Input    2
    Input    foo
    Input    bar
    Input    Koira
    Input    kaksituhattakymmenen
    Input    Q
    Run and Quit
    Output Should Contain    year

*** Keywords ***
Run And Quit
    Input    0
    Run Application

Delete Reference
    Input    3
    Input    Testiavain
