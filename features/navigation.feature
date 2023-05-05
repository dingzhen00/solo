Feature: Navigation

  Scenario: Navigate through the website
    Given I am on the homepage
    When I click on "Go to all products page"
    Then I should be on the product list page
    When I go back to the homepage
    When I click on "Registration"
    Then I should be on the registration page
    When I go back to the homepage
    When I click on "Login"
    Then I should be on the login page
    When I go back to the homepage
    When I click on "Administrator Login"
    Then I should be on the admin login page
