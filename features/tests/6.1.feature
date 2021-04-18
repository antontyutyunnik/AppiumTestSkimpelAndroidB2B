# Created by anton at 17.04.2021
Feature: Adding an event / selecting a photo for the menu from the smartphone library
  # Enter feature description here

  Scenario: Adding an event / selecting a photo for the menu from the smartphone library
    Given Tap on application language EU 6.1
    When Enter email EU 6.1
    When Enter password EU 6.1
    When Click on the "Sign in" button EU 6.1
    When Profile page is open EU 6.1
    When Press the add event button EU 6.1
    When Click add photo EU 6.1
    When Press the button with Choose from Library EU 6.1
    When Click Google Photos EU 6.1
    When Click on the Downloads folder EU 6.1
    When Select photo EU 6.1
    When Enter the name of the event EU 6.1
    When Enter event description EU 6.1
    When Enter event date EU 6.1
    When Enter event time EU 6.1
    When Enter event price EU 6.1
    When Click Save EU 6.1
    Then Click OK EU 6.1