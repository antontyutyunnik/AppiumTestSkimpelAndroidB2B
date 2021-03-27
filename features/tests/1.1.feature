# Created by anton at 24.03.2021
Feature: Selecting the application language EU
  # Enter feature description here

  Scenario: Selecting the application language EU
    Given Tap on application language EU 1.1
    When  Scroll to the bottom of the page EU 1.1
    When  Click on the button "I agree" EU 1.1
    Then login page is open EU 1.1