# Created by anton at 24.03.2021
Feature: Selecting the application language DE
  # Enter feature description here

  Scenario: Selecting the application language DE
    Given Tap on application language DE 1.2
    When  Scroll to the bottom of the page DE 1.2
    When  Click on the button "I agree" DE 1.2
    Then login page is open DE 1.2