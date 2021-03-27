# Created by anton at 26.03.2021
Feature: Log in to the app with valid data
  # Enter feature description here

  Scenario: Log in to the app with valid data
    Given Tap on application language EU 2.1
    When Enter email EU 2.1
    When Enter password EU 2.1
    When Click on the "Sign in" button EU 2.1
    Then Profile page is open EU 2.1
