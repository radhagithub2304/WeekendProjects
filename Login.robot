*** Settings ***
Library  SeleniumLibrary
*** Variables ***

*** Test Cases ***
Login to facebook
    open browser  http://facebook.com  chrome
    input text  id=email  Testname
    input text  id=pass  Anu
*** Keywords ***
