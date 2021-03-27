# Created by anton at 21.03.2021
Feature: Login for Skimpel B2B
  # Enter feature description here

  Scenario: User enters the application
    Given Tap on application language
    When  Enter Email and Password and click on Sign in
    Then  Show account User