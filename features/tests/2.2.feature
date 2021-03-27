# Created by anton at 26.03.2021
Feature: Log in to the app with not valid data
  # Enter feature description here

  Scenario: Log in to the app with an unregistered email
    Given Tap on application language EU 2.2
    When Enter email EU 2.2
    When Enter password EU 2.2
    Then Click on the "Sign in" button EU 2.2
    Then Email or password is not correct EU 2.2