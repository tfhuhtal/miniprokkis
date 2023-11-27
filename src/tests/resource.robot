*** Settings ***
Library  ../AppLibrary.py

*** Variables ***
${DELAY}  1.0 seconds

*** Keywords ***

Run App
    Run Application

Input List References
    Input Text  2
    Input  ENTER