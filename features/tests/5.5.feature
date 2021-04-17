# Created by anton at 17.04.2021
Feature: Remove category using three dots
  # Enter feature description here

  Scenario: Remove category using three dots
    Given Tap on application language EU 5.5
    When Enter email EU 5.5
    When Enter password EU 5.5
    When Click on the "Sign in" button EU 5.5
    When Profile page is open EU 5.5
    When Press the menu button EU 5.5
    When Click button edit category EU 5.5
    Then Click delete category EU 5.5