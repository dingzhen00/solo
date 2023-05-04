Feature: User sign-in

  Scenario: User signs in with valid credentials
    Given I am on the "sign-in" page
    When I enter "john" as the username
    And I enter "password123" as the password
    And I click the "Submit" button
    Then I should be redirected to the "product-list" page

  Scenario: User signs in with invalid credentials
    Given I am on the "sign-in" page
    When I enter "john" as the username
    And I enter "wrongpassword" as the password
    And I click the "Submit" button
    Then I should see an error message

  Scenario: User leaves username or password field blank
    Given I am on the "sign-in" page
    When I leave the username or password field blank
    And I click the "Submit" button
    Then I should see an error message

