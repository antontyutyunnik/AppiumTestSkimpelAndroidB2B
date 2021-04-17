# Created by anton at 17.04.2021
Feature: Remove product from category
  # Enter feature description here

  Scenario: Remove product from category
    Given Tap on application language EU 5.6
    When Enter email EU 5.6
    When Enter password EU 5.6
    When Click on the "Sign in" button EU 5.6
    When Profile page is open EU 5.6
    When Press the menu button EU 5.6
    When Press the category name EU 5.6
    Then Delete product in category EU 5.6